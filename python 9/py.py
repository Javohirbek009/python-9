# #Dunder methodi ---- murakkab klaslar bn iwlash
# class Numbers:
    
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
        
#     def __add__(self,value):
#         return Numbers(self.num1 + value.num1, self.num2 + value.num2)

#     def __repr__(self):
#         return f"num1 ning qiymati: {self.num1} va num2 ning qiymati: {self.num2}"

# log = Numbers(10, 10)
# log2 = Numbers(20, 20)
# log3 = Numbers(30, 30)

# print(log + log2 + log3)

# murakkab funksiyalar


def decorative_function(func):
    def ichki(malumotlar):
        return [func(value[0], value[1]) for value in malumotlar]
    return ichki


@decorative_function
def num(a, b):
    print(a + b)

print(num([(10, 20), (20, 20), (30, 30)]))


####

def decorative_function(func):
    def cont(values):
        return [func(value[0], value[1]) for value in values]
    return cont


@decorative_function
def num1(a, b):
    print(a - b)

print(num1([(50, 20), (45, 10), (30, 30)]))


####

def decorative_function(func):
    def cont1(values1):
        return [func(value[0], value[1]) for value in values1]
    return cont1


@decorative_function
def num2(a, b):
    print(a * b)

print(num2([(50, 2), (45, 3), (30, 5)]))


####

def decorative_function(func):
    def cont2(values2):
        return [func(value[0], value[1]) for value in values2]
    return cont2


@decorative_function
def num3(a, b):
    print(a / b)

print(num3([(50, 2), (145, 3), (150, 5)]))