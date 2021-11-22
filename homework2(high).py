
print('математические действия')

n = int(input())
print(n)
s = str(n)
sm = 0
for i in range(len(s)):
    sm += int(s[i])
print("summ=" + str(sm))

sub = 0
for i in range(len(s)):
    sub -= int(s[i])
print("вычитание=" + str(sub))
