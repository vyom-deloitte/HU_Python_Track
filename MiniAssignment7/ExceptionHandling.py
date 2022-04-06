#Custom calculator
class FormulaError(Exception):
    pass
def parse_input(user_input):

  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Invalid Input,input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('Invalid Input,the first and third input value must be numbers')
  return n1, op, n2


def calculator(input1, operator, input2):

    if operator == '+':
            return input1 + input2
    elif operator == '-':
            return input1 - input2
    else:
        raise FormulaError('Invalid Input,operator should be only + or -')


while True:
  user_input = input('Perform operation: ')
  if user_input == 'exit':
    break
  input1, operator, input2 = parse_input(user_input)
  ans = calculator(input1, operator, input2)
  print("Output: ",ans)