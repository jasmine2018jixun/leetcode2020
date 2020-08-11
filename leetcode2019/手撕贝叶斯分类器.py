import sys
import numpy as np
from collections import defaultdict
# 训练数据为15个样本
x1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
x2 = [1, 2, 2, 1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 3, 3]
y = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
input = np.column_stack([x1, x2, y])

# 求样本点（2，1）的类别
new_data = [2, 1]


class Bayes_Classifier(object):
    '''

    构造朴素贝叶斯分类器

    '''
    def __init__(self, input, new_data):
        self.x = input[:, :-1]
        self.y = input[:, -1]
        self.prior_prob = self.compute_prior_prob()
        self.x1_d0, self.x1_d1 = self.compute_cond_prob(0)
        self.x2_d0, self.x2_d1 = self.compute_cond_prob(1)
        self.test_data = new_data

        
    def compute_prior_prob(self):
        '''

        先验概率的极大似然估计

        '''
        prior_prob = defaultdict(int)
        for i in range(len(self.y)):
            if self.y[i] == -1:
                prior_prob[-1] += 1
            else:
                prior_prob[1] += 1
        for key in prior_prob.keys():
            prior_prob[key] /= len(self.y)
    
        return prior_prob


    def compute_cond_prob(self, j):
        '''

        条件概率的极大似然估计
        <类确定的条件下，特征j取某值的概率>

        '''
        d0 = defaultdict(int)
        y0 = 0
        d1 = defaultdict(int)
        y1 = 0
        for n in range(self.x.shape[0]):
            if self.y[n] == -1:
                d0[self.x[n, j]] += 1
                y0 += 1
            else:
                d1[self.x[n, j]] += 1
                y1 += 1
        for key, value in d0.items():
            d0[key] = value / y0
        for key, value in d1.items():
            d1[key] = value / y1
        return d0, d1
    
    def max_pos_prob(self):
        '''

        最大化后验概率
        
        '''
        p0 = self.x1_d0[self.test_data[0]] * self.x2_d0[self.test_data[1]] * self.prior_prob[-1]
        p1 = self.x1_d1[self.test_data[0]] * self.x2_d1[self.test_data[1]] * self.prior_prob[1]
        return p0, p1


bayes = Bayes_Classifier(input, new_data)
# print(bayes.unique_y)
# print(bayes.x1_d0, bayes.x2_d0)
# print(bayes.x1_d1, bayes.x2_d1)
# print(bayes.prior_prob)
print(bayes.max_pos_prob())