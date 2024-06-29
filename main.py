def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)

    for i in range(2,N):
        next = a1 + a2
        result.append(next)
        a1, a2 = a2, next
        
    print(result)


    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
