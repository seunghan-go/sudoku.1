import copy

# for replacement
# output is array[9][9]
def getInput():
    print("Type in given number from top left. type 0 if it is unknown")
    initValue = list()
    i = 1
    while i <10:
        val = input("Row %d :" %i)
        temp = val.split(" ")
        if len(temp) is 9:
            initValue.append(temp)
        else:
            print("Number of nums should be 9")
            i = i - 1
        i += 1
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
    initValue2 = [ 
        [8, 0, 0, 0, 7, 0, 6, 2, 0 ],
        [0, 0, 0, 0, 9, 6, 0, 7, 8 ],
        [0, 6, 0, 8, 0, 0, 3, 0, 5 ],
        [0, 9, 0, 6, 0, 8, 0, 0, 0 ],
        [3, 0, 0, 0, 0, 0, 0, 0, 6 ],
        [0, 0, 0, 2, 0, 1, 0, 3, 0 ],
        [9, 0, 7, 0, 0, 4, 0, 6, 0 ],
        [2, 5, 0, 9, 8, 0, 0, 0, 0 ],
        [0, 3, 4, 0, 6, 0, 0, 0, 2 ],
        ]
    initValue3 = [ 
        [0, 0, 0, 9, 3, 0, 4, 8, 0 ],
        [3, 0, 6, 8, 2, 0, 0, 0, 0 ],
        [5, 9, 8, 0, 1, 0, 0, 0, 3 ],
        [0, 2, 5, 0, 0, 3, 0, 0, 9 ],
        [9, 0, 7, 5, 0, 1, 3, 0, 0 ],
        [6, 3, 0, 0, 9, 0, 0, 5, 8 ],
        [7, 6, 9, 0, 5, 0, 8, 3, 1 ],
        [0, 0, 0, 3, 7, 9, 6, 0, 0 ],
        [0, 0, 3, 1, 6, 8, 0, 0, 0],
        ]
    initValue4 = [ 
        [0, 0, 0, 5, 6, 0, 0, 0, 3 ],
        [0, 0, 3, 0, 0, 0, 8, 0, 1 ],
        [7, 0, 0, 0, 3, 2, 0, 5, 0 ],
        [4, 0, 9, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 6, 0, 7, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 3, 0, 9 ],
        [0, 5, 0, 2, 1, 0, 0, 0, 6 ],
        [2, 0, 8, 0, 0, 0, 9, 0, 0 ],
        [3, 0, 0, 0, 8, 9, 0, 0, 0 ]
        ]
    initValue4 = [ 
        [0, 0, 0, 0, 9, 5, 7, 0, 0 ],
        [0, 0, 2, 0, 7, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 1, 2, 4 ],
        [7, 0, 0, 0, 0, 0, 0, 8, 0 ],
        [0, 0, 9, 8, 0, 4, 2, 0, 0 ],
        [0, 3, 0, 0, 0, 0, 0, 0, 5 ],
        [8, 5, 1, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 2, 0, 6, 0, 0 ],
        [0, 0, 7, 1, 3, 0, 0, 0, 0 ]        
        ]
    print(initValue2)
    return initValue4

class sudoku:
    candidateMap = list()

    def _init_reslutData(self):
        self.resultRow = [[] for i in range(9)]
        self.resultCol = [[] for i in range(9)]
        self.resultSquare = [[] for i in range(9)]

    def __init__(self, initValue):
        self.resultMap = copy.deepcopy(initValue)
        self._initCandidateMap()
        self._init_reslutData()

    def _initCandidateMap(self):
        for i in range(9):
            self.candidateMap.append([])
            for j in range(9):
                if self.resultMap[i][j] > 0:
                    self.candidateMap[i].append([])
                else:
                    self.candidateMap[i].append([1,2,3,4,5,6,7,8,9])
#        print(self.candidateMap)


    def updateResultData(self):
        self._init_reslutData()
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
                for i in range(3):
                    for j in range(3):
                        if self.resultMap[x+i][y+j] > 0:
                            self.resultSquare[idx].append(self.resultMap[x+i][y+j])
                idx+=1

 #   def __checkRowsWith2Lines(self, i, j):
    def _next1(self, i):
        return (int(i/3))*3+(i+1)%3

    def _next2(self, i):
        return (int(i/3))*3+(i+2)%3

    def _influence(self):  # 이건 간단하게 추론인데.. 3x3 공간에서 가로든 세로든 하나 남아있는 블럭의 경우, 옆줄에 후보들이 다 있는 경우는 그 수가 된다.
        #3x3 안에 혼자있는걸 체크해야지.
        for i in range(9):
            for j in range(9):
                if self.resultMap[i][j] is 0:
                    if self.resultMap[i][self._next1(j)] > 0 and self.resultMap[i][self._next2(j)] >0 : ## 그 줄에 유일하게 비어있는가. 비었다면..
                        # 3줄을 처리할 것임.
                        for value in self.candidateMap[i][j]:
                            if value in self.resultRow[self._next1(i)] and value in self.resultRow[self._next2(i)]:
                                self.resultMap[i][j] = value
                                self.updateResultData()
                                self.updateCandidateMap()
                                break
            
                    # 세로방향으로 체크한번 하고
                    if self.resultMap[self._next1(i)][j] > 0 and self.resultMap[self._next2(i)][j] >0 : ## 그 줄에 유일하게 비어있는가. 비었다면..
                        for value in self.candidateMap[i][j]:
                            if value in self.resultCol[self._next1(j)] and value in self.resultCol[self._next2(j)]:
                                self.resultMap[i][j] = value
                                self.updateResultData()
                                self.updateCandidateMap()
                                break
            
        return True

    def _influence2(self): # 한줄에, candidate 수를 다 체크해보면 그중 한개만 있는건 그거다.
        #가로부터 보자
        for i in range(9):
            for k in range(1,9):
                temp = 0
                idx = -1
                if k not in self.resultRow[i]:
                    for j in range(9):
                        if k in self.candidateMap[i][j]:
                            temp += 1
                            idx = j
                            if temp is 2:
                                break;
                    if temp is 1:
                        self.resultMap[i][idx] = k
                        self.updateResultData()
                        self.updateCandidateMap()
                        break
        # 세로로 보자
        for j in range(9):
            for k in range(1,9):
                temp = 0
                idx = -1
                if k not in self.resultCol[j]:
                    for i in range(9):
                        if k in self.candidateMap[i][j]:
                            temp += 1
                            idx = i
                            if temp is 2:
                                break;
                    if temp is 1:
                        self.resultMap[idx][j] = k
                        self.updateResultData()
                        self.updateCandidateMap()
                        break


        return True

    def _influence3(self): # 세번째인데, 비슷한 소린데, 빈칸들의 candiate중 유일하게 한칸에만 있는 놈은 거기다. 
        return True

    def _square(sef, i, j):
        return int(i/3)*3+int(j/3)

    def updateCandidateMap(self):
        # 현재 셀의 위치 기준으로 x축 y축의 resultMap(확정된 값)을 candidate에서 제거.
        # 현재 셀 속해있는 square안의 확정된 값 제거.
        # 단순하게 이렇게 다 지웠는데 삭제한 놈의 length가 1이 되면 resultMap 업데이트 하고 candidate에서 제거.
        ret = False

        for i in range(9):
            for j in range(9):
                if self.resultMap[i][j] is 0:
                    currentCandidate = self.candidateMap[i][j] 
                    for x in self.resultRow[i]:
                        if x in currentCandidate:
                            currentCandidate.remove(x)
                            ret = True
                    for x in self.resultCol[j]:
                        if x in currentCandidate:
                            currentCandidate.remove(x)
                            ret = True
                    for x in self.resultSquare[self._square(i,j)]:
                        if x in currentCandidate:
                            currentCandidate.remove(x)
                            ret = True
                    if len(currentCandidate) is 1:
                        self.resultMap[i][j] = currentCandidate.pop()
                        self.updateResultData()
                        ret = True
                else:
                    self.candidateMap[i][j] = []

        return ret


    
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
            while self.updateCandidateMap() is True:
                pass
            ### 그러다 하나만 남으면 그걸 가지고 resultMap 업데이트.
            self._influence()
            self._influence2()

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

    #values = getInput()
    values = testInput()
    getResult(values)
    #printResult()

