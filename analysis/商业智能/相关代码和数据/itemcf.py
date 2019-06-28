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


class ItemBasedCF(object):
    ''' TopN recommendation - Item Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_movie = 20
        self.n_rec_movie = 10

        self.movie_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        print('Similar movie number = %d' % self.n_sim_movie, file=sys.stderr)
        print('Recommended movie number = %d' %
              self.n_rec_movie, file=sys.stderr)

    def generate_dataset(self,train_data,test_data):
        ''' load rating data and split it to training set and test set '''
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


        print('split training set and test set succ', file=sys.stderr)
        print('train set = %s' % train_len, file=sys.stderr)
        print('test set = %s' % test_len, file=sys.stderr)

    def calc_movie_sim(self):
        ''' calculate movie similarity matrix '''#评估产品相似度
        print('counting movies number and popularity...', file=sys.stderr)

        for user, movies in self.trainset.items():
            for movie in movies:
                # count item popularity
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1

        print('count movies number and popularity succ', file=sys.stderr)

        # save the total number of movies
        self.movie_count = len(self.movie_popular)
        print('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated users between items在项目之间计数共同用户 
        itemsim_mat = self.movie_sim_mat
        print('building co-rated users matrix...', file=sys.stderr)

        for user, movies in self.trainset.items():
            for m1 in movies:
                itemsim_mat.setdefault(m1, defaultdict(int))
                for m2 in movies:
                    if m1 == m2:
                        continue
                    itemsim_mat[m1][m2] += 1

        print('build co-rated users matrix succ', file=sys.stderr)

        # calculate similarity matrix计算相似度矩阵 
        print('calculating movie similarity matrix...', file=sys.stderr)
        simfactor_count = 0
        PRINT_STEP = 2000000

        for m1, related_movies in itemsim_mat.items():
            for m2, count in related_movies.items():
                itemsim_mat[m1][m2] = count / math.sqrt(
                    self.movie_popular[m1] * self.movie_popular[m2])
                simfactor_count += 1
                if simfactor_count % PRINT_STEP == 0:
                    print('calculating movie similarity factor(%d)' %
                          simfactor_count, file=sys.stderr)

        print('calculate movie similarity matrix(similarity factor) succ',
              file=sys.stderr)
        print('Total similarity factor number = %d' %
              simfactor_count, file=sys.stderr)

    def recommend(self, user):
        ''' Find K similar movies and recommend N movies. '''
        K = self.n_sim_movie #相似用户
        N = self.n_rec_movie #推荐用户
        rank = {}
        watched_movies = self.trainset[user]

        for movie, rating in watched_movies.items():
            for related_movie, similarity_factor in sorted(self.movie_sim_mat[movie].items(),
                                                           key=itemgetter(1), reverse=True)[:K]: #预测用户对每个产品的兴趣并排序
                if related_movie in watched_movies:
                    continue
                rank.setdefault(related_movie, 0)
                rank[related_movie] += similarity_factor * rating
        # return the N best movies
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]

    def evaluate(self):
        ''' print evaluation result: precision, recall, coverage and popularity '''
        print('Evaluation start...', file=sys.stderr)

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

 

        for i, user in enumerate(self.trainset):
            if i % 500 == 0:
                print ('recommended for %d users' % i, file=sys.stderr)
            test_movies = self.testset.get(user, {})
            rec_movies = self.recommend(user)
            #for movie, _ in rec_movies:
                #if movie in test_movies:
                    #hit += 1
                #all_rec_movies.add(movie)
                #popular_sum += math.log(1 + self.movie_popular[movie])
            #rec_count += N
            #test_count += len(test_movies)
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
        #print(true_list,pred_list)
        precision, recall, threshold = precision_recall_curve(true_list, pred_list)
 
              
        plt.title("itemcf-PR.png")
        
        plt.figure(1)
   
        plt.ylim([0,0.2])     
        plt.plot(recall, precision)
        
        plt.show()
        
        plt.savefig('itemcf-PR.png')

   