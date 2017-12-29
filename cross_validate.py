
import random

import string



#Training
pos_file = "hotelT-train.txt"
neg_file = "hotelF-train.txt"


pf = open(pos_file)

nf = open(neg_file)

pos_lines_list = []
neg_lines_list = []

for line in pf:
    pos_lines_list.append(line)
for line in nf:
    neg_lines_list.append(line)
train_ratio = 0.8
test_ratio = 0.2

k = int(1/test_ratio)

train_number = int(train_ratio*(len(pos_lines_list)+len(neg_lines_list)))
test_number = (len(pos_lines_list)+len(neg_lines_list)) - train_number

pos_train_number = int(train_number/2)
neg_train_number = train_number - pos_train_number

pos_test_number = int(test_number/2)
neg_test_number = test_number - pos_test_number

#print train_number, test_number
#print pos_train_number, neg_train_number, pos_test_number, neg_test_number

pos_indices = range(0, len(pos_lines_list))
random.shuffle(pos_indices)
#print pos_indices

neg_indices = range(0, len(neg_lines_list))
random.shuffle(neg_indices)
#print neg_indices
accuracies = []

for iti in range(0, k):
    si = (pos_test_number * iti)
    ei = (pos_test_number * (iti + 1))
    # print si
    # print ei
    pos_test_indices = pos_indices[si:ei]
    pos_train_indices = [item for item in pos_indices if item not in pos_test_indices]
    # print(len(test_indices))
    # print "----"
    # writing test file
    gold_file = open(str(iti + 1) + "gold_file", "w")
    test_file = open(str(iti + 1) + "test_samples", "w")
    for sentence_num in pos_test_indices:
      gold_file.write(pos_lines_list[sentence_num].split()[0]+" T\n")
      test_file.write(pos_lines_list[sentence_num])

    # writing train file
    train_file = open(str(iti + 1) + "pos_train_samples", "w")
    for sentence_num in pos_train_indices:
       train_file.write(pos_lines_list[sentence_num])
    si = (neg_test_number * iti)
    ei = (neg_test_number * (iti + 1))
    # print si
    # print ei
    neg_test_indices = neg_indices[si:ei]
    neg_train_indices = [item for item in neg_indices if item not in neg_test_indices]
    # print(len(test_indices))
    # print "----"
    # writing test file

    for sentence_num in neg_test_indices:
        gold_file.write(neg_lines_list[sentence_num].split()[0] + " F\n")
        test_file.write(neg_lines_list[sentence_num])

    # writing train file
    train_file = open(str(iti + 1) + "neg_train_samples", "w")
    for sentence_num in neg_train_indices:
        train_file.write(neg_lines_list[sentence_num])

    '''naive.naive_bayes(iti)
    gold_file = open(str(iti + 1) + "gold_file", "r")
    output_file = open(str(iti + 1) + "output_samples", "r")
    gold_dic = {}
    output_dic = {}
    for line in gold_file:
        words = line.strip().split()
        gold_dic[words[0]] = words[1]
    for line in output_file:
        words = line.strip().split()
        output_dic[words[0]] = words[1]
    correct = 0
    for word in output_dic.keys():
        if output_dic[word] == gold_dic[word]:
            correct += 1
    #print(correct)
    acc = correct/float(len(output_dic.keys()))
    print "Accuracy for ", iti+1, " is ",acc
    accuracies.append(acc)
print "Average accuracy is ", sum(accuracies)/len(accuracies)'''















