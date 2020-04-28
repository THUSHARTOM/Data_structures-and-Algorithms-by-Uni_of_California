# python3

def max_num(numbers):
    n = len(numbers)
    max_index_a = -1


    for i in range(n):

        if  (max_index_a == -1) or (numbers[i] > numbers[max_index_a]):
            max_index_a = i

    max_index_b = -1

    for j in range(n):
        if ((j != max_index_a) and  ((max_index_b == -1) or (numbers[j] > numbers[max_index_b]))):
            max_index_b = j

    return numbers[max_index_b] * numbers[max_index_a]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_num(input_numbers))








