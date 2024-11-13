import inspect

def test():
    pass

def introspection_info(obj):
    print(f'Тип объекта: {type(obj)}')
    print(f'Атрибуты и методы объекта: {dir(obj)}')
    print(f'Модуль: {inspect.getmodule(obj)}')
    print(f'Уникальный идентификатор: {id(obj)}')
    print(f'Вызываемость: {callable(obj)}')


introspection_info(42)
