terminology={
    'value_name': "字母数字下划线,是赋予value的标签，指向特定的值",
    'traceback' : 'a record to point out whats wrong',
    'string':'用引号扩出来的',
    'method':'对数据执行的操作，后面跟圆括号',
    'f_string':'use value in strings',
    'constance':'名称全部大写',
    'list' :'方括号中间，有序，index从0开始',
    'append' : '在list末尾加value',
    'insert' : "在list任何位置加，需要index，lover.insert(0.'cat')",
    'del' : "del lover[0]",
    'pop' : 'delete list 末尾元素，并能继续使用 lover.pop(1)',
    'remove' : "delete 知道值的元素 remove('cat')"
    }
print(f"value_name\n\t{terminology['value_name']}")
print(f'traceback\n\t{terminology["traceback"]}')
print(f'string\n\t{terminology["string"]}')
print(f'method\n\t{terminology["method"]}')

for name, explaination in terminology.items():
    print(f"{name.title()}:\n\t{explaination}")

