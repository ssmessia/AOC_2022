raw='''Sensor at x=251234, y=759482: closest beacon is at x=-282270, y=572396
Sensor at x=2866161, y=3374117: closest beacon is at x=2729330, y=3697325
Sensor at x=3999996, y=3520742: closest beacon is at x=3980421, y=3524442
Sensor at x=3988282, y=3516584: closest beacon is at x=3980421, y=3524442
Sensor at x=3005586, y=3018139: closest beacon is at x=2727127, y=2959718
Sensor at x=3413653, y=3519082: closest beacon is at x=3980421, y=3524442
Sensor at x=2900403, y=187208: closest beacon is at x=2732772, y=2000000
Sensor at x=1112429, y=3561166: closest beacon is at x=2729330, y=3697325
Sensor at x=3789925, y=3283328: closest beacon is at x=3980421, y=3524442
Sensor at x=3991533, y=3529053: closest beacon is at x=3980421, y=3524442
Sensor at x=3368119, y=2189371: closest beacon is at x=2732772, y=2000000
Sensor at x=2351157, y=2587083: closest beacon is at x=2727127, y=2959718
Sensor at x=3326196, y=2929990: closest beacon is at x=3707954, y=2867627
Sensor at x=3839244, y=1342691: closest beacon is at x=3707954, y=2867627
Sensor at x=2880363, y=3875503: closest beacon is at x=2729330, y=3697325
Sensor at x=1142859, y=1691416: closest beacon is at x=2732772, y=2000000
Sensor at x=3052449, y=2711719: closest beacon is at x=2727127, y=2959718
Sensor at x=629398, y=214610: closest beacon is at x=-282270, y=572396
Sensor at x=3614706, y=3924106: closest beacon is at x=3980421, y=3524442
Sensor at x=3999246, y=2876762: closest beacon is at x=3707954, y=2867627
Sensor at x=3848935, y=3020496: closest beacon is at x=3707954, y=2867627
Sensor at x=123637, y=2726215: closest beacon is at x=-886690, y=3416197
Sensor at x=4000000, y=3544014: closest beacon is at x=3980421, y=3524442
Sensor at x=2524955, y=3861248: closest beacon is at x=2729330, y=3697325
Sensor at x=2605475, y=3152151: closest beacon is at x=2727127, y=2959718'''

from collections import defaultdict
raw = raw.splitlines()
positions = []
for r in raw:
    t1 = (int(r[r.find('x=')+2:r.find(',')]), int(r[r.find('y=')+2:r.find(':')]))
    t2 = (int(r[r.rfind('x=')+2:r.rfind(',')]), int(r[r.rfind('y=')+2:]))
    positions.append(t1+t2)
    
'''
huge search space (in the trillions of positions), can't simulate entire space
for each position, get Manhattan distance, calculate list of positions it can't be append to dict[y] = [x,]
  that was still way too slow, only do it for the row you need (2000000)
    manhattan = abs(x1-x2) + abs(y1-y2)
    for i in range(1,manhattan):
        for j in range(manhattan-2000000):
            P[y1+i].append(x1+j)
            P[y1-i].append(x1+j)
    Answers: 4529072 (too low), 5636463(too low), 5688616, 5688619
'''

P = defaultdict(list)
for p in positions:
    x1, y1, x2, y2 = p
    manhattan = abs(x1-x2) + abs(y1-y2)
    dist_away = abs(y1-2000000)
    if dist_away <= manhattan:
        for i in range(manhattan-dist_away+1):
            P[2000000].append(x1+i)
            P[2000000].append(x1-i)

print(len(list(set(P[2000000])))-1) #there is a beacon at y=2000000

#need something non-quadratic

#generate all points that are just outside the Manhattan distance
#iterate through those to see if they are within a sensors Manhattan distance
P = defaultdict(list)
possibles = []
for p in positions:
    print(p)
    x1, y1, x2, y2 = p
    manhattan = abs(x1-x2) + abs(y1-y2)
    for i in range(manhattan+1):
        left, right = x1-manhattan+1-i, x1+manhattan+1-i
        if left < 0: left = 0
        if right > 4000000: right = 4000000
        if 0 <= y1+i <= 4000000:
          possibles.append((left, y1+i))
          possibles.append((right, y1+i))
        if 0 <= y1-i <= 4000000:
          possibles.append((left, y1+i))
          possibles.append((right, y1+i))

goal = len(positions)
for pos in possibles:
    total = 0
    for p in positions:
        x1, y1, x2, y2 = p
        dist = abs(x1-pos[0]) + abs(y1-pos[1])
        manhattan = abs(x1-x2) + abs(y1-y2)
        if dist > manhattan:
            total+=1
    if total == goal:
        print(pos, pos[0]*4000000+pos[1]) 

#could never get this to work

#remove ranges where it can't be from 0-4000000 (this would still take too long)
#lowest/highest it can't be for each row
#for each sensor, for each manhattan dist
'''
#start with a tuple (0,4000000), then remove from it and see what's left
for i in range(4000001):
    T = [(0, 4000000)] #range of possible locations
    for p in P[i]:
        #print(T,p)
        low, high = p
        for t in T: 
            if t[0] ==  4000000 or t[1] == 0:
                T.remove(t)        
            elif low<=t[0] and t[1]<=high and (t[0] != t[1]): #tuple is covered, remove
                T.remove(t)
            elif t[0] <= low <= high <= t[1]: #separate into two tuples:
                lower, upper = (t[0],low-1), (high+1,t[1])
                T.append(lower)
                T.append(upper)
                T.remove(t)
            elif t[0] <= high <=t[1]: #raise lower end
                new = (high+1, t[1])
                T.append(new)
                T.remove(t)
            elif low <= t[1] <= high: #lower higher end
                new = (t[0], low-1)
                T.append(new)
                T.remove(t)
    if T: print(i,T)
'''

        
       
