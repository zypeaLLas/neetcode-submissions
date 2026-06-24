class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        if operations[0].lstrip('-').isdigit():
            record.append(int(operations[0]))
            for i in range(1,len(operations)):
                if(operations[i].lstrip('-').isdigit()):
                    record.append(int(operations[i]))
                elif (operations[i] == 'D'):
                    record.append(record[-1] *2)
                elif (operations[i] == '+'):
                    record.append(record[-1]+ record[-2])
                elif (operations[i] == 'C'):
                    record.pop(-1)
        return sum(record)