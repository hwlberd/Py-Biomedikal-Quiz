x = [
    ['A', '-', 'T', 'T', 'G', '-', 'C', 'T', 'T'],
    ['A', 'C', 'C', 'T', 'G', 'G', 'C', '-', 'T'],
    ['A', 'C', 'T', 'A', '-', 'G', 'C', 'T', 'A'],
    ['A', 'G', 'T', 'A', 'G', 'C', 'A', 'T', 'T']
]
sums0 = 0
sums1 = 0
sums2 = 0

for i in range(3):

    for j in range(9):

        match i:
            case 0:

                if x[i][j] == '-' or x[i + 1][j] == '-':
                    sums0 -= 1

                elif x[i][j] == x[i + 1][j]:
                    sums0 += 3

                elif x[i][j] != x[i + 1][j]:
                    sums0 += 2

                if x[i][j] == '-' or x[i + 2][j] == '-':
                    sums0 -= 1

                elif x[i][j] == x[i + 2][j]:
                    sums0 += 3

                elif x[i][j] != x[i + 2][j]:
                    sums0 += 2

                if x[i][j] == '-' or x[i + 3][j] == '-':
                    sums0 -= 1

                elif x[i][j] == x[i + 3][j]:
                    sums0 += 3

                elif x[i][j] != x[i + 3][j]:
                    sums0 += 2
            case 1:

                if x[i][j] == '-' or x[i + 1][j] == '-':
                    sums1 -= 1

                elif x[i][j] == x[i + 1][j]:
                    sums1 += 3

                elif x[i][j] != x[i + 1][j]:
                    sums1 += 2

                if x[i][j] == '-' or x[i + 2][j] == '-':
                    sums1 -= 1

                elif x[i][j] == x[i + 2][j]:
                    sums1 += 3

                elif x[i][j] != x[i + 2][j]:
                    sums1 += 2

            case 2:

                if x[i][j] == '-' or x[i + 1][j] == '-':
                    sums2 -= 1

                elif x[i][j] == x[i + 1][j]:
                    sums2 += 3

                elif x[i][j] != x[i + 1][j]:
                    sums2 += 2

print("sum of pairs skoru :", sums0+sums1+sums2)




