class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if ( len(operations) == 1):
            return int(operations[0])
        record = []
        total = 0
        current_record=1
        if operations[0].lstrip('-').isdigit():
            record.append(int(operations[0]))
            for i in range(1,len(operations)):
                if(operations[i].lstrip('-').isdigit()):
                    record.append(int(operations[i]))
                    current_record +=1
                    continue
                elif (operations[i] == 'D'):
                    record.append(record[current_record-1] *2)
                    current_record +=1
                    continue
                elif (operations[i] == '+'):
                    record.append(record[current_record-1]+ record[current_record-2])
                    current_record+=1
                    continue
                elif (operations[i] == 'C'):
                    record.pop(current_record - 1)
                    current_record-=1
                    continue
            #calculate the record's total
            for value in record:
                total += value
            return total