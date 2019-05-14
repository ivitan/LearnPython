import nltk
import csv

nltk.download()
# 导入数据
SMMSS = open('SMSSpamCollectionjsn.txt','r',encoding='utf-8')
sms_data,sms_label = [],[]
csv_reader = csv.reader(SMMSS,delimiter = '\t')
for line in csv_reader:
    sms_data.append(line[0])
    sms_label.append(line[1])
SMMSS.close()

print(sms_data,sms_label)

# 数据清洗
sms_label = str(sms_label)
sms_label = sms_label.lower()
sms_label = sms_label.split()
sms_label_affter = []
for i in sms_label:
    print(i)
    if len(i) < 4:
        sms_label_affter.append(i)
print(sms_label_affter)

