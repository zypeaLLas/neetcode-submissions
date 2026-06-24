class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if ( len(operations) == 1):
            return int(operations[0])
        record = []
        total = 0

        if operations[0].lstrip('-').isdigit():
            record.append(int(operations[0]))
            for i in range(1,len(operations)):
                if(operations[i].lstrip('-').isdigit()):
                    record.append(int(operations[i]))

                    continue
                elif (operations[i] == 'D'):
                    record.append(record[-1] *2)

                    continue
                elif (operations[i] == '+'):
                    record.append(record[-1]+ record[-2])

                    continue
                elif (operations[i] == 'C'):
                    record.pop(-1)

                    continue
            #calculate the record's total
            for value in record:
                total += value
            return total