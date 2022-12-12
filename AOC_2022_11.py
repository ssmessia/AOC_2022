'''Monkey 0:
  Starting items: 85, 77, 77
  Operation: new = old * 7
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 7

Monkey 1:
  Starting items: 80, 99
  Operation: new = old * 11
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 5

Monkey 2:
  Starting items: 74, 60, 74, 63, 86, 92, 80
  Operation: new = old + 8
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 3:
  Starting items: 71, 58, 93, 65, 80, 68, 54, 71
  Operation: new = old + 7
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 4:
  Starting items: 97, 56, 79, 65, 58
  Operation: new = old + 5
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 77
  Operation: new = old + 4
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 6:
  Starting items: 99, 90, 84, 50
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 7:
  Starting items: 50, 66, 61, 92, 64, 78
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 1
'''
monkeys = [[85, 77, 77],[80, 99],
        [74, 60, 74, 63, 86, 92, 80],[71, 58, 93, 65, 80, 68, 54, 71],
        [97, 56, 79, 65, 58],[77],
        [99, 90, 84, 50],[50, 66, 61, 92, 64, 78]]
modulos = [19,3,13,7,5,11,17,2]
operations = [[6,7],[3,5],[0,6],[2,4],[2,0],[4,3],[7,1],[5,1]]
counts = [0,0,0,0,0,0,0,0]

F = {0:lambda x:x*7, 1: lambda x:x*11, 2: lambda x:x+8, 3: lambda x:x+7,
     4: lambda x:x+5, 5: lambda x:x+4, 6: lambda x:x*x, 7: lambda x:x+3}

for i in range(20):
    for j in range(8):
        length = len(monkeys[j])
        for n in range(length):
            counts[j]+=1
            temp = monkeys[j].pop(0)
            temp = F[j](temp)//3
            if temp % modulos[j] == 0:
                monkeys[operations[j][0]].append(temp)
            else:
                monkeys[operations[j][1]].append(temp)
counts = sorted(counts)
print(counts[-1]*counts[-2])

LCM = 19*3*13*7*5*11*17*2
print(LCM)

monkeys = [[85, 77, 77],[80, 99],
        [74, 60, 74, 63, 86, 92, 80],[71, 58, 93, 65, 80, 68, 54, 71],
        [97, 56, 79, 65, 58],[77],
        [99, 90, 84, 50],[50, 66, 61, 92, 64, 78]]
counts = [0,0,0,0,0,0,0,0]
for i in range(10000):
    for j in range(8):
        length = len(monkeys[j])
        for n in range(length):
            counts[j]+=1
            temp = monkeys[j].pop(0)
            temp = F[j](temp) %LCM
            if temp % modulos[j] == 0:
                monkeys[operations[j][0]].append(temp)
            else:
                monkeys[operations[j][1]].append(temp)
counts = sorted(counts)
print(counts)
print(counts[-1]*counts[-2])
