#-*- coding: utf-8 -*-
import sys
import random
import math
import os
from operator import itemgetter

from sklearn.metrics import precision_recall_curve
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
random.seed(0)


class UserBasedCF(object):
    ''' TopN recommendation - User Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_user = 20
        self.n_rec_movie = 10

        self.user_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        print ('Similar user number = %d' % self.n_sim_user, file=sys.stderr)
        print ('recommended movie number = %d' %
               self.n_rec_movie, file=sys.stderr)

    def generate_dataset(self,train_data,test_data):
        
        train_len = train_data.shape[0]
        
        test_len = test_data.shape[0]

        
        for index, row in train_data.iterrows():
            
            user = row['UserNo']
            
            movie = row['ProgramNo']
            
            rating = row['Score']
            
            self.trainset.setdefault(user, {})
            
            self.trainset[user][movie] = int(rating)
        
        for index, row in test_data.iterrows():
            
            user = row['UserNo']
            
            movie = row['ProgramNo']
            
            rating = row['Score']
            
            self.testset.setdefault(user, {})
            
            self.testset[user][movie] = int(rating)
        
        print ('split training set and test set succ', file=sys.stderr)
        
        print ('train set = %s' % train_len, file=sys.stderr)
        
        print ('test set = %s' % test_len, file=sys.stderr)

    def calc_user_sim(self):  #相似度区别
        ''' calculate user similarity matrix '''
        # build inverse table for item-users
        # key=movieID, value=list of userIDs who have seen this movie
        print ('building movie-users inverse table...', file=sys.stderr)
        movie2users = dict()

        for user, movies in self.trainset.items():
            for movie in movies:
                # inverse table for item-users项目用户倒数表
                if movie not in movie2users:
                    movie2users[movie] = set()
                movie2users[movie].add(user)
                # count item popularity at the same time同时统计项目的知名度 
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        print ('build movie-users inverse table succ', file=sys.stderr)

        # save the total movie number, which will be used in evaluation
        self.movie_count = len(movie2users)
        print ('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated items between users计算用户之间的共评级物品数-用户评分
        usersim_mat = self.user_sim_mat
        print ('building user co-rated movies matrix...', file=sys.stderr)

        for movie, users in movie2users.items():  #设置默认值default
            for u in users:
                usersim_mat.setdefault(u, defaultdict(int))
                for v in users:
                    if u == v:
                        continue
                    usersim_mat[u][v] += 1
        print ('build user co-rated movies matrix succ', file=sys.stderr)

        # calculate similarity matrix评估相似度
        print ('calculating user similarity matrix...', file=sys.stderr)
        simfactor_count = 0
        PRINT_STEP = 2000000

        for u, related_users in usersim_mat.items():
            for v, count in related_users.items():
                usersim_mat[u][v] = count / math.sqrt(
                    len(self.trainset[u]) * len(self.trainset[v]))
                simfactor_count += 1
                if simfactor_count % PRINT_STEP == 0:
                    print ('calculating user similarity factor(%d)' %
                           simfactor_count, file=sys.stderr)

        print ('calculate user similarity matrix(similarity factor) succ',
               file=sys.stderr)
        print ('Total similarity factor number = %d' %
               simfactor_count, file=sys.stderr)

    def recommend(self, user):
        ''' Find K similar users and recommend N movies. '''
        K = self.n_sim_user
        N = self.n_rec_movie
        rank = dict()
        watched_movies = self.trainset[user]

        for similar_user, similarity_factor in sorted(self.user_sim_mat[user].items(),
                                                      key=itemgetter(1), reverse=True)[0:K]:
            for movie in self.trainset[similar_user]:
                if movie in watched_movies:
                    continue
                # predict the user's "interest" for each movie
                rank.setdefault(movie, 0)
                rank[movie] += similarity_factor
        # return the N best movies
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]

    def evaluate(self):
        ''' print evaluation result: precision, recall, coverage and popularity '''
        print ('Evaluation start...', file=sys.stderr)

        N = self.n_rec_movie
        #  varables for precision and recall
        hit = 0
        rec_count = 0
        test_count = 0
        # varables for coverage
        all_rec_movies = set()
        # varables for popularity
        popular_sum = 0
        true_list = []
        
        pred_list = []

         
        #上市enumerate
        for i, user in enumerate(self.trainset):
            if i % 500 == 0:
                print ('recommended for %d users' % i, file=sys.stderr)
            test_movies = self.testset.get(user, {})
            rec_movies = self.recommend(user)
            for movie, score in rec_movies:
                pred_list.append(score)


                if movie in test_movies:
                    hit += 1
                    true_list.append(1)
                else:
                    true_list.append(0)
                #all_rec_movies.add(movie)
                popular_sum += math.log(1 + self.movie_popular[movie])
            rec_count += N
            test_count += len(test_movies)

        precision = hit / (1.0 * rec_count)
        recall = hit / (1.0 * test_count)
        coverage = len(all_rec_movies) / (1.0 * self.movie_count)
        popularity = popular_sum / (1.0 * rec_count)
        TP = hit
        FP = rec_count-hit
        FN = test_count-hit
        TN = N-FP-FN+TP

        print ('precision=%.4f\trecall=%.4f\tcoverage=%.4f\tpopularity=%.4f' %
               (precision, recall, coverage, popularity), file=sys.stderr)
        print('TP=%.4f\tFP=%.4f\tFN=%.4f\tTN=%.4f\t'%(TP,FP,FN,TN))
        
        precision, recall, threshold = precision_recall_curve(true_list, pred_list)
  
        #print(true_list,pred_list)      
        plt.title("usercf-p-r.png")
        
        plt.figure(1)
   
        plt.ylim([0,0.2])     
        plt.plot(recall, precision)
        
        plt.show()
        
        plt.savefig('usercf-PR.png')

       





