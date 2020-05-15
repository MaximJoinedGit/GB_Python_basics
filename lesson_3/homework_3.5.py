"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""


def sum_until(user_input, lst):
    """
    Function accepts input from user. It adds all the numbers with using the loop from user input until special symbol
    'x' appears in user input. All the other symbols will be ignored with according message.
    :param user_input: all possible symbols including letters.
    :type user_input: list
    :param lst: only numbers which were in user input.
    :type lst: list
    :return: list of numbers.
    """
    for num in user_input:
        if not num == special:
            try:
                lst.append(int(num))
            except ValueError:
                print('В последовательности встретилось не число и не специальный символ. Мы его пропустили.')
        else:
            break
    return lst


nums = []
special = 'x'
all_nums = []

while special not in nums:
    nums = input().split(' ')
    result = sum_until(nums, all_nums)
    print(sum(result))
