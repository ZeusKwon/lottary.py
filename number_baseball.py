from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers



def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    a = 1
    while len(new_guess)<3:
        new_number = int(input("{}번째 숫자를 입력하세요.".format(a)))
        if new_number<0 or new_number>9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        elif new_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        else:
            new_guess.append(new_number)
        a += 1

    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count
    
ANSWER = generate_numbers()
print(ANSWER)
tries = 0
while True:
    tries += 1

    number = take_guess()
    st_count, bl_count = get_score(number, ANSWER)
    if st_count == 3:
        break
    else:
        print("{0}S {1}B".format(st_count, bl_count))

# 코드를 작성하세요.

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))