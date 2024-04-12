def check(letter):
    arr=[]
    for let in letter:
        if let in arr:
            return True
        arr.append(let)
    return False



print('Lets see: with Take')
print(check('Take'))
print('Lets see: with Hello')
print(check('Hello'))