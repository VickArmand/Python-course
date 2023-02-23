details = ('1', 'Aryaman', 'Computer Science')
 
def func(roll_no, name, branch):
    print(f'Roll number {roll_no} is {name} from {branch} branch of Engineering.') 
 
func(*details)