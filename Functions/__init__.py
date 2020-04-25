from client import Client
from account import Account

print('Enter your details:')
client1 = Client(str(input('Name:')), int(input('CPF: ')), int(input('Age: ')))
user1 = Account(client1, float(input('Account Balance: ')), float(input('Account Limit: ')))


def line():
    print('-' * 50)

# Defines the title
def title(msg):
    line()
    print(msg.center(50))
    line()

# Print a menu in the first moment.
def menu():
    print('Choose your option: \n'
          '1 - Account Balance\n'
          '2 - Withdram Money\n'
          '3 - Deposit:\n'
          '4 - Exit')
    line()
    option_choosed()

# Here we can see the Banking System options, where people can choose what they want to do.
def option_choosed():
    opt = str(input('What is your option: '))
    line()
    while opt not in '12345':
        opt = str(f'Wrong option. Try again!\n'
                  f'What is your option: ')
        line()
    if opt == '1':
        return f'{user1.account_balance()}', line(), contin()

    elif opt == '2':
        value = float(input('How much do you want to whithdraw? R$: '))
        user1.withdraw_money(value)
        print(f'You made a withdrawal from R$:{value}')
        return f'Your balance is R$:{user1.account_balance()}', line(), contin()

    elif opt == '3':
        value = float(input('How much do you want to deposit: R$:'))
        user1.deposit(value)
        print(f'You made a deposit of R$:{value}')
        return f'Your balance is R$:{user1.account_balance()}', line(), contin()
    elif opt == '4':
        while True:
            print('See you soon!')
            break

# Ask users if they want to continue.
def contin():
    try:
        answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
        line()
    except:
        print('Wrong Option!\n'
              'Try again.')
        line()
        return contin()
    else:
        while answer not in 'YN':
            print('Wrong Option!\n'
                  'Try again.')
            line()
            return contin()
        if answer == 'Y':
            return title('BANK SYSTEM'), menu()
        else:
            while answer == 'N':
                print('See you soon!')
                line()
                break
