class Sort:

    def __init__(self, numbers: list):
        self.numbers = numbers

    def partition(self, lst):
        if len(lst) <= 1:
            return lst
        element = lst[0]
        left = list(filter(lambda num: num < element, lst))
        center = [num for num in lst if num == element]
        right = list(filter(lambda num: num > element, lst))

        return self.partition(left) + center + self.partition(right)

    def quick_sort(self):
        if len(self.numbers) <= 1:
            return self.numbers
        element = self.numbers[0]
        left = list(filter(lambda num: num < element, self.numbers))
        center = [num for num in self.numbers if num == element]
        right = list(filter(lambda num: num > element, self.numbers))

        return self.partition(left) + center + self.partition(right)

    def __str__(self):
        return f"List of numbers: {self.numbers}\n"


num = Sort(numbers=[6, 1, 51, 25, 42])
print(num)
print(num.quick_sort())