from functools import reduce

# 1. Create a function that receives a function and a number, and returns the result of applying the function to the number.
def add_value(f, value):
    return f(value)

print(add_value(lambda n: n - 2, 9))

# 2. Create a function that receives two numbers and a function, and returns the result of adding the two numbers and applying the function.
def sum_func(n1, n2, f):
    return f(n1 + n2)

print(sum_func(4, 8, lambda x: x ** 2))

# 3. Create a function that returns another function that adds a fixed number.
def static_num(a):
    return lambda b: b + a

add_four = static_num(4)

print(add_four(12))

# 4. Use map() with lambda to multiply each number in a list by 10.
these_numb = [3, 25, 17, 8, 13, 22]
total = list(map(lambda m: m * 10, these_numb))
print(total)

# 5. Use filter() with lambda to keep only the even numbers.
pairs = list(filter(lambda p: p % 2 == 0, these_numb))
print(pairs)

# 6. Use reduce() with lambda to obtain the total sum of a list.
total_sum = reduce(lambda r, xyz: r + xyz, these_numb)
print(total_sum)

# 7. Write a function that returns a function that receives a name and returns "Hello, ".
def greet(intro):
    return lambda name: intro + name if len(name) != 0 else "Introduce a name"

changing = greet("Hi ")

print(changing(""))

# 8. Create a function that receives a list and a function, and counts how many elements satisfy the function.
partners = [ "Lua", "Garret", "Aoife", "Ailbhe", "Patrick", "Kate"]

def count_if(names, condition):
    count = []
    for name in names:
        if condition(name):
            count.append(name)
    return count

result = count_if(partners, lambda name: len(name) > 5)

print(result)


# 9. Create a function that receives two functions and a number, and applies them in order.
def marrige(func1, func2, number):
    result_first = func1(number)
    result_second = func2(result_first)
    return result_second

bridge_part = lambda x: x * 10 // 2
groom_part = lambda y: y + 20 * 15 // 3
friends = 250 // 25

print(marrige(bridge_part, groom_part, friends))


# 10. Create a function that receives a list and a function, and applies that function to each element using a loop (without map).
def impacting_list(list, f):
    total = []
    for i in list:
        total.append(f(i))
    return total

print(impacting_list([6, 7, 8, 9], lambda x: x + 5))