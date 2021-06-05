"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
import types


def instances_counter(cls):

    cls.count_of_obj = 0

    def __init__(*args, **kwargs):
        cls.count_of_obj += 1
        object.__new__(cls, *args, **kwargs)

    def get_created_instances(cls):
        return cls.count_of_obj

    def reset_instances_counter(cls):
        output = cls.count_of_obj
        cls.count_of_obj = 0
        return output

    cls.__init__ = types.MethodType(__init__, cls)

    cls.get_created_instances = types.MethodType(get_created_instances, cls)

    cls.reset_instances_counter = types.MethodType(reset_instances_counter, cls)

    return cls


if __name__ == "__main__":
    ...
