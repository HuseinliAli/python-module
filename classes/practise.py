class Practise:
    def __init__(self, number1, number2, message) -> None:
        self.number1 = number1
        self.number2 = number2
        self.message = message
        
    def sum_two_nums(self):
        return self.number1 + self.number2
    
    def print_message(self):
        print(self.message)
        
    def sum_of_list(self,numbers:list):
        return sum(numbers)
    
    def avg_of_list(self,numbers:list):
        self.numbers = numbers
        return sum(numbers) / len(numbers)