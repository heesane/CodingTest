from copy import deepcopy
import time
import random
N,M =map(int,input().split(' '))
rc = []
for n in range(N):
    rc.append(random.randrange(1000,1100))
start_time = time.time()
max_rc = max(rc) - 1
start = 0
while start <= max_rc:
    rc_dup = deepcopy(rc)
    total = 0
    mid = (start + max_rc) // 2
    for i in range(N):
        rc_dup[i] = rc[i] - mid
        if rc_dup[i] < 0:
            rc_dup[i] = 0
    total = sum(rc_dup)
    if total < M:
        max_rc = mid - 1
    elif total > M:
        start = mid +1
    else:
        break
end_time = time.time()
print(max_rc)
print("%s"%(end_time - start_time))
        