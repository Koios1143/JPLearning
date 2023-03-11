# Predefine some variables
RED = '\033[91m' #RED
RESET = '\033[0m' #RESET COLOR 
ClassName = ['', 'accent_plain', 'accent_top']

if __name__ == '__main__':
    # Information of this script
    print('This is a simple tool to mark accent by yourself easily.')

    while True:
        Sentence = input('Input the Sentence: ')
        Result = []
        for i in range(len(Sentence)):
            Char = Sentence[i]
            if(i != 0):
                print(Sentence[:i], end='')
            print(RED + Sentence[i] + RESET, end='')
            if(i != len(Sentence)):
                print(Sentence[i+1:], end='')
            print()

            if(Char in '、。！？'):
                Result.append('<span>{}</span>'.format(Char))
            else:
                Option = int(input('Input Accent (0: None, 1: Normal, 2: Down): '))
                while(Option not in [0, 1, 2]):
                    Option = int(input('Try Again (0: None, 1: Normal, 2: Down): '))
                if(Option == 0):
                    Result.append('<span>{}</span>'.format(Char))
                else:
                    Result.append('<span class="{}">{}</span>'.format(ClassName[Option], Char))
        
        # Process Done, Print All Result
        print('========== Result ==========')
        for i in Result:
            print(i, end='')
        print()
        
        # Next Query or not
        Next = '@'
        End = False;
        while(Next not in ['y', 'Y', 'n', 'N']):
            Next = input('End of this query. Next query? (y/n)')
            if(Next in ['y', 'Y']):
                break
            elif(Next in ['n', 'N']):
                End = True
                break
            else:
                continue
        if(End):
            break