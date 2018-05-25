from sklearn.naive_bayes import MultinomialNB
import numpy as np

#d1: hanoi pho chaolong hanoi
#d2: hanoi buncha pho omai
#d3: pho banhgio omai
#d4: saigon hutiu banhbo pho
#d5: hanoi hanoi buncha hutiu
#d6: pho hutiu banhbo
#d7: saigon pho hutiu
#V={hanoi, pho, chaolong, buncha, omai, banhgio, saigon, hutiu, banhbo}
d1 = [2,1,1,0,0,0,0,0,0]
d2 = [1,1,0,1,1,0,0,0,0]
d3 = [0,1,0,0,1,1,0,0,0]
d4 = [0,1,0,0,0,0,1,1,1]
d5 = [2,0,0,1,0,0,0,1,0]
d6 = [0,1,0,0,0,0,0,1,1]
d7 = [0,1,0,0,0,0,1,0,0]

train_data = np.array([d1, d2, d3, d4])
test_data = np.array([d5])
test_d6 = np.array([d6])
test_d7 = np.array([d7])
label = np.array(['B', 'B', 'B','N'])

clf = MultinomialNB()
clf.fit(train_data, label)

print(clf.predict(test_data))
print("d6", clf.predict(test_d6))
print("d7", clf.predict(test_d7))