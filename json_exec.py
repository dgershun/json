import json
import pdb
#pdb.set_trace()
#implemented linear +, -, *, /, &&, ||, >, <, ==, if, input, goto


def get_by_path(data, array):
    current_path = data
    for i in range(len(array)):
        current_path = current_path[array[i]]
    return current_path

def set_to_path(data, array, element):
    current_path = data
    for i in range(len(array)-1):
        current_path = current_path[array[i]]
    current_path[array[-1]] = element

def binary_operation(current, text):
    left = current['left']
    right = current['right']
    if left['type'] == "pointer":
        left = get_by_path(text, left['path'])
        right = get_by_path(text, right['path'])
        return left, right

# годится только для поинтеров вида ["program", 0].
# надо переделать на более общий случай
def get_next(next):
    if next == "end":
        return "end"
    elif next['type'] == "pointer":
        prog['current_address'] = next['path']
        # возвращается text['program'][number], а если уровень глубже? TODO?
        # подумать, стоит ли каждый раз передавать program
        return text[next['path'][0]][next['path'][1]]
        
def stack_push(element):
    text['stack'].insert(0, element);
    

f = open('prog.json', 'r')
text = json.loads(str(f.read()))
f.close()


print(json.dumps(text))
prog = text['program']
# входная точка
next = get_next(prog['current_address'])
while (next != "end"):
    current = next
    if current['type'] == "linear_plus":
        left, right = binary_type(current, text)
        current['result'] = left + right
        next = get_next(current['next'])
    elif current['type'] == "linear_minus":
        left, right = binary_type(current, text)
        current['result'] = left - right
        next = get_next(current['next'])
    elif current['type'] == "linear_mult":
        left, right = binary_type(current, text)
        current['result'] = left * right
        next = get_next(current['next'])
    # не забыть про дробные
    elif current['type'] == "linear_div":
        left, right = binary_type(current, text)
        current['result'] = left / right
        next = get_next(current['next'])
    elif current['type'] == "linear_and":
        left, right = binary_type(current, text)
        current['result'] = left and right
        next = get_next(current['next'])
    elif current['type'] == "linear_or":
        left, right = binary_type(current, text)
        current['result'] = left or right
        next = get_next(current['next'])
    elif current['type'] == "linear_more":
        left, right = binary_type(current, text)
        current['result'] = left > right
        next = get_next(current['next'])
    elif current['type'] == "linear_less":
        left, right = binary_type(current, text)
        current['result'] = left < right
        next = get_next(current['next'])
    elif current['type'] == "linear_equal":
        left, right = binary_type(current, text)
        current['result'] = left == right
        next = get_next(current['next'])
    elif current['type'] == "linear_if":
        if current['condition']['type'] == "pointer":
            condition = get_by_path(text, current['condition']['path'])
            if condition == True:
                next = get_next(current['if_true']['next'])
            if condition == False:
                next = get_next(current['if_false']['next'])
    elif current['type'] == "linear_input":
        print(data)
        address = input('input address (without key data, example:"number4" ): ')
        user_input = input('input data: ')
        set_to_path(data, address.split(':'), user_input)
        next = get_next(current['next'])
    elif current['type'] == "linear_goto":
        next = get_next(current['address'])
    else current['type'] == "recursive_add":
        stack_el = {}
        stack_el['type'] = "operation"
        stack_el['operation'] = "recursive_add"
        stack_el['address']
        if current['left']['type'] == "pointer":
        else
            stack_el['right'] = current['right']
            text['data'] = stack_push(stack_el, text['stack'])
            next = current['left']

print("\n\n\n")
print(json.dumps(text))
