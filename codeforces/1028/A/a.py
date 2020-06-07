# https://codeforces.com/contest/1028/submission/82875061
n, m = map(int, input().split())

for i in range(n):
  line = input()
  c = line.count('B')
  j = line.find('B')
  if j != -1:
    print("{} {}".format(i + c//2 + 1, j + c//2 + 1))
    break
