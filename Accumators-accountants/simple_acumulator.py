
color = {
    'White':'\033[1;97m',
    'Reset':'\033[0m'
}
#===================================================================

sum = 0

while True:
    n = int(input(f'Type a number to sum {color['White']}[ press 0 to quit. ]{color['Reset']}: '))
    if n == 0:
        break
    sum += n
print(f'The total sum amount is {sum}')