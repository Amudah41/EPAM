"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    class Wrapper(cls):
        cls.count_of_obj = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.count_of_obj += 1

        @classmethod
        def get_created_instances(cls):
            return cls.count_of_obj

        @classmethod
        def reset_instances_counter(cls):
            output = cls.count_of_obj
            cls.count_of_obj = 0
            return output

    return Wrapper


if __name__ == "__main__":
    ...
