N = int(input())
word_list = []
exist_list = []
for _ in range(N):
    word = input()
    word_list.append([len(word),word])
word_list.sort()
word_list.sort(key = len)
for i in range(len(word_list)):
    if word_list[i][1] not in exist_list:
        exist_list.append(word_list[i][1])
        print(word_list[i][1])
    else:
        continue