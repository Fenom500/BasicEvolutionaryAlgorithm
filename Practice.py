import random

# all functions predefined


def gen_number(maxnum):
    while len(numbers) < maxnum:
        # generate a random number as an integer
        num_int = random.randint(0, 128)
        # convert it to 8-bit binary
        num = num_to_bin(num_int)
        # add it to relevant arrays(integer array is primarily for debugging purposes/avoiding constant conversions)
        numbers.append(num)
        integers.append(num_int)


def num_to_bin(int_input):
    num = str(bin(int_input))
    # convert the string to a 8 bit int(because str(bin()) only gives the relevant bits
    num = num.split("b")[1]
    length = len(num)
    start_string = "0"
    while len(start_string) < 8-length:
        start_string = start_string+"0"
    if int_input < 128:
        num = start_string+num
    return num


def natural_selection():
    # delete the smallest number from both numbers array and integers array
    minimum = min(integers)
    min_index = integers.index(minimum)
    numbers.pop(min_index)
    integers.pop(min_index)


def offspring():
    length = len(numbers)
    parent1 = numbers[random.randint(0, length-1)]
    parent2 = numbers[random.randint(0, length-1)]
    parent1 = list(parent1)
    parent2 = list(parent2)
    genome = zip(parent2, parent1)
    child = []
    for gene in genome:
        child.append(gene[random.randint(0, 1)])
    child = "".join(child)
    numbers.append(child)
    integers.append(int(child, 2))


def mutate():
    # pick a random entry in the list on numbers
    index1 = random.randrange(len(numbers))
    genome = list(numbers[index1])
    # remove them until after the mutation occurs
    numbers.pop(index1)
    integers.pop(index1)
    # choose a random gene to mutate
    index2 = random.randrange(8)
    # generate replacement gene randomly
    genome[index2] = str(random.randint(0,1))
    genome = "".join(genome)
    #restore the entries to the list
    numbers.append(genome)
    integers.append(int(genome,2))

# generation, create x random 8 bit numbers
    # x is the number of "creatures" in every step that follows offspring or is before natural selection
x = 3
    # max pop is the amount remaining after natural selection
max_pop = 2
numbers = []
integers = []
gen = 0
mutation_rate = 3
gen_number(x)


while max(integers) < 255:
    gen += 1
    print(gen)
    while len(numbers) > max_pop:
        natural_selection()
    print(integers)
    while len(numbers) < x:
        offspring()
    mutations = 0
    print(integers)
    while mutations < mutation_rate:
        mutations += 1
        mutate()
    print(integers)
    print("\n")
