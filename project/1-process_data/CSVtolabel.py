# coding=utf-8
"""
根据上一步骤得到的CSV文件，将搜索文本以及三个属性剥离，保存为相应的文件
注意路径
"""
import pandas as pd
import os
WORK_DIR = '/Users/gaobellen/WorkSpace/sourcedata/sougou-user-profile'
#path of the train and test files
trainname = os.path.join(WORK_DIR, 'user_tag_query.10W.TRAIN.csv')
testname = os.path.join(WORK_DIR, 'user_tag_query.10W.TEST.csv')

data = pd.read_csv(trainname)
print data.info()

#generate three labels for age/gender/education
data.age.to_csv(os.path.join(WORK_DIR, "train_age.csv"), index=False)
data.Gender.to_csv(os.path.join(WORK_DIR, "train_gender.csv"), index=False)
data.Education.to_csv(os.path.join(WORK_DIR, "train_education.csv"), index=False)
#generate trainfile's text file
data.QueryList.to_csv(os.path.join(WORK_DIR, "train_querylist.csv"), index=False)

data = pd.read_csv(testname)
print data.info()
#generate testfile's text file
data.QueryList.to_csv(os.path.join(WORK_DIR, "test_querylist.csv"), index=False)
