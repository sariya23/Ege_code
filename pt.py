def win1(x, s):
    if x + s < 47 and ((47 <= s + x + 2 <= 59) or (47 <= 3*x + s <= 59) or (47 <= x + 3*s <= 59)) or x + s > 59:
        return True
    return False


def loss1(x, s):
    if not(win1(x, s)) and win1(x + 2, s) and win1(x, s + 2) and win1(3*x, s) and win1(x, 3*s):
        return True
    return False


def win2(x, s):
    return loss1(x + 2, s) or loss1(x, s + 2) or loss1(3*x, s) or loss1(x, 3*s)


def loss12(x, s):
    if (win1(x + 2, s) or win2(x + 2, s)) and (win1(x, s + 2) or win2(x, s + 2)) and (win1(3*x, s) or win2(3*x, s)) and \
            (win1(x, 3*s) or win2(x, 3*s)) and (win1(x + 2, s) or win1(x, s + 2) or win1(3*x, s) or win1(x, 3*s)) and \
            (win2(x + 2, s) or win2(x, s + 2) or win2(3 * x, s) or win2(x, 3 * s)):
        return True
    return False


x = 5
s19 = []
s20 = []
s21 = []

for s in range(1, 42):
    if win1(x, s + 2) and win1(x + 2, s) and win1(3*x, s) and win1(x, 3*s):
        s19.append(s)
    if win2(x, s):
        s20.append(s)
    if loss12(x, s):
        s21.append(s)
print(s19)
print(s20)
print(s21)
