# Link: https://www.hackerrank.com/challenges/magic-square-forming/problem

idea = '''
Each cell will have different value in the range of [1, 9]
The magic constant will always be 15

We need to turn every square back into the standard 1.
8 3 4
1 5 9
6 7 2

How to turn it back to the standard one and how to minimize cost?

- Notice the four corner of the standard 1 => 8, 6, 4, 2
- The center one has to be 5
- Then notice the adjacent cell of each corner.

*** need to know the position of each corner and standard adjacent cells to each corner

*** method:
- create the circle of cells in the right order: [2, 9, 4, 3, 8, 1, 6, 7] => start with a corner
- then how to turn the circle from the problem into the standard one? will it need to be with the corner again?
- which corner to start the circle?
'''


def formingMagicSquare(square):
    cost = 60  # just put a big value here

    # print out 4 corners:
    cellsCircleStandard = [2, 9, 4, 3, 8, 1, 6, 7]

    row1 = square[0]
    row2 = square[1]
    row3 = square[2]
    center = row2[1]

    # create the cells circle from the top right of the square
    # clock wise and counter clock wise
    cellsCircleCW = row1 + [row2[2]] + list(reversed(row3)) + [row2[0]]
    cellsCircleCounterCW = list(reversed(row1)) + [row2[0]] + row3 + [row2[2]]
    #
    # print("Center is:", row2[1])
    # print("Circle ClockWise:", cellsCircleCW)
    # print("Circle Counter ClockWise:", cellsCircleCounterCW)

    # we need to compare the cellsCircle 4 times with the standard one.
    for i in range(4):
        tempCW = abs(center - 5)
        tempCounterCW = abs(center - 5)

        tempCircleCW = cellsCircleCW[i * 2:] + cellsCircleCW[:i * 2]
        tempCircleCounterCW = cellsCircleCounterCW[i * 2:] + cellsCircleCounterCW[:i * 2]
        for j in range(len(tempCircleCW)):
            standardCell = cellsCircleStandard[j]

            cellCW = tempCircleCW[j]
            cellCounterCW = tempCircleCounterCW[j]

            tempCW += abs(cellCW - standardCell)
            tempCounterCW += abs(cellCounterCW - standardCell)

        if min(tempCW, tempCounterCW) < cost:
            cost = min(tempCW, tempCounterCW)
    return cost


if __name__ == "__main__":
    with open("Input") as f:
        cases = int(f.readline())
        for i in range(cases):
            square = []
            for j in range(3):
                row = list(map(int, f.readline().rstrip().split()))
                print(row)
                square.append(row)
            result = formingMagicSquare(square)
            print("Cost:", result)
            print()
            # print(square)
