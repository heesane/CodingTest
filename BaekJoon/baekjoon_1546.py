N = int(input())
subject = list(map(int,input().split(' ')))
high_score = max(subject)
for i in range(len(subject)):
    subject[i] = subject[i] / high_score * 100
mean = sum(subject) / N
print(mean)