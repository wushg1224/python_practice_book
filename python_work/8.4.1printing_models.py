#首先创建一个列表，其中一个包含需要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahendron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model : {current_design}")
    completed_models.append(current_design)

print(f'The following models have been printed:')
for completed_model in completed_models:
    print(completed_model)



#use function to do the same thing




def print_models(unprinted_designs, completed_models):
    """"
    模拟打印每个设计，直到没有未打印设计为止
    打印每个设计后，都将其移到completed_models列表中
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """"显示打印好的模型"""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

#function_name(list_name_[:])