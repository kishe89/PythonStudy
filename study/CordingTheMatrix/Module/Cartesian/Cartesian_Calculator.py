

# 카테시안 결과값 클래스
class Cartesian_result:
    size = None
    result = None
    resultString = None

    def __init__(self):
        self

    def setValue(self, result, size, resultString):
        self.size = size
        self.result = result
        self.resultString = resultString


# 카테시안 계산 클래스
class Cartesian_Calculator:

    S1 = None
    S2 = None
    result = None

    def __init__(self, S1, S2):
        """
            This function initialize Cartesian_Calculator class
            @type  self: self
            @param self: self
            @type  S1: list
            @param S1: 집합
            @type  S2: list
            @param S2: 집합
            """
        self.S1 = S1
        self.S2 = S2
        self.result = Cartesian_result()

    # 집합 카테시안 곱 결과 포맷된 문자열 반환함수
    def Product(self):
        """
            This function executes Cartesian Product and then returns Object,
            which contains the result and size (cardinality) and a String.
            @type  self: self
            @param self: self
            @rtype:   Cartesian_result
            @return:  Object contain result, cardinality, String
            """
        if self.S1 is None:
            return None
        if self.S2 is None:
            return None

        print('Input Parameter 1 ' + str(self.S1))
        print('Input Parameter 2 ' + str(self.S2))
        itemGroup = []
        for aItem in self.S1:
            for bItem in self.S2:
                abItem = [aItem, bItem]
                itemGroup.append(abItem)
                resultString = '집합 A = ' + str(self.S1)
                resultString += ', 집합 B = ' + str(self.S2)
                resultString += '에 대해, 카테시안(Cartesian product) 곱은 '
                resultString += str(itemGroup) + '이고 '
                resultString += '크기는 ' + str(len(itemGroup)) + ' 이다.'
        self.result.setValue(itemGroup, len(itemGroup), resultString)
        return self.result
