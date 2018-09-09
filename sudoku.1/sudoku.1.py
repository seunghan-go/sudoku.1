import copy

# for replacement
# output is array[9][9]
def getInput():
    print("Type in given number from top left. type 0 if it is unknown")
    initValue = list()
    for i in range(10):
        val = input("Row %d :" %i)
        temp = val.split(" ")
        if len(temp) is 9:
            initValue.append(temp)
        else:
            print("Number of nums should be 9")
            i = i - 1
        print(initValue)
    return initValue

def testInput():
    initValue = [ 
        [8, 0, 4, 6, 0, 3, 1, 0, 0 ],
        [0, 3, 5, 7, 0, 0, 0, 0, 0 ],
        [7, 0, 0, 0, 1, 0, 0, 0, 3 ],
        [6, 0, 1, 0, 4, 0, 7, 0, 5 ],
        [0, 4, 0, 0, 0, 0, 0, 6, 0 ],
        [5, 0, 2, 0, 8, 0, 9, 0, 1 ],
        [3, 0, 0, 0, 2, 0, 0, 0, 4 ],
        [0, 0, 0, 0, 0, 8, 6 ,5, 0 ],
        [0, 0, 8, 4, 0, 5, 3, 0, 9 ],
        ]
    print(initValue)
    return initValue

class sudoku:
    candidateMap = list()

    def init_reslutData(self):
        self.resultRow = [[] for i in range(9)]
        self.resultCol = [[] for i in range(9)]
        self.resultSquare = [[] for i in range(9)]

    def __init__(self, initValue):
        self.resultMap = copy.deepcopy(initValue)
        self.initCandidateMap()
        self.init_reslutData()

    def initCandidateMap(self):
        for i in range(9):
            self.candidateMap.append([])
            for j in range(9):
                if self.resultMap[i][j] > 0:
                    self.candidateMap[i].append([])
                else:
                    self.candidateMap[i].append([1,2,3,4,5,6,7,8,9])
        print(self.candidateMap)


    def updateResultData(self):
        self.init_reslutData()
        for i in range(9):
            for j in range(9):
                if j+1 in self.resultMap[i]:
                    self.resultRow[i].append(j+1)

        for j in range(9):
            for i in range(9):
                if self.resultMap[i][j] > 0:
                    self.resultCol[j].append(self.resultMap[i][j])

        idx=0
        for x in range(0,9,3): # square는 좌상단부터 012 345 678 로 하자
            for y in range(0,9,3):
                tempList = []
                for i in range(3):
                    for j in range(3):
                        if self.resultMap[x+i][y+j] > 0:
                            self.resultSquare[idx].append(self.resultMap[x+i][y+j])
                idx+=1


    def updateCandidateMap(self):
        # 현재 셀의 위치 기준으로 x축 y축의 resultMap(확정된 값)을 candidate에서 제거.
        # 현재 셀 속해있는 square안의 확정된 값 제거.
        # 단순하게 이렇게 다 지웠는데 삭제한 놈의 length가 1이 되면 resultMap 업데이트 하고 candidate에서 제거.

        for i in range(9):
            for j in range(9):
                if self.resultMap[i][j] is 0:
                    for x in self.resultRow[i]:
                        if x in self.candidateMap[i][j]:
                            self.candidateMap[i][j].remove(x)
                    if len(self.candidateMap[i][j]) is 1:
                        self.resultMap[i][j] = self.candidateMap[i][j].pop()

                    for x in self.resultCol[j]:
                        if x in self.candidateMap[i][j]:
                            self.candidateMap[i][j].remove(x)
                    if len(self.candidateMap[i][j]) is 1:
                        self.resultMap[i][j] = self.candidateMap[i][j].pop()

                    num = int((i/3)*3) + int(j/3)
                    num1 = i/3
                    num2 = int(i/3)
                    num3 = int(i/3)*3
                    num4 = (int(i/3))*3
                    num5 = int((i/3)*3)
                    for x in self.resultSquare[int(i/3)*3+int(j/3)]:
                        if x in self.candidateMap[i][j]:
                            self.candidateMap[i][j].remove(x)
                    if len(self.candidateMap[i][j]) is 1:
                        self.resultMap[i][j] = self.candidateMap[i][j].pop()


    def isFinished(self):
        for i in range(9):
            #if self.resultMap[i].index(0) >= 0:
            if 0 in self.resultMap[i]:
                return False
        return True

    def doGame(self):
        while self.isFinished() is False:
            # 우선 resultMap 을 기반으로 각 row별, column별, square별로 확정된 값을 만들고
            self.updateResultData()
            ## candidate에서 그것들을 제거.
            self.updateCandidateMap()
            ### 그러다 하나만 남으면 그걸 가지고 resultMap 업데이트.


    def getResult(self):
        self.doGame()
        return self.resultMap

    def printResultMap(self):
        for i in self.resultMap:
            print(i)
        print("\n")

def getResult(values):
    game = sudoku(values)
    result = game.getResult()
    game.printResultMap()

    return result

if __name__ == "__main__":
    print("sudoku__")

    #getInput()
    values = testInput()
    getResult(values)
    #printResult()

