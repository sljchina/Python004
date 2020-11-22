# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。--OK
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，
# 是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。--OK
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，
# 除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    def __init__(self,animal_type,shape,nature):
        self.animal_type = animal_type
        self.shape = shape
        self.nature = nature
        if ((shape == '中等' or shape == '大型') and (animal_type == '食肉类型')):
            self.is_fierce_animal = True
        else:
            self.is_fierce_animal = False
        # return self.is_fierce_animal
    def fierce_animal(self):
        return self.is_fierce_animal

    @abstractmethod
    def animal_call(self):
        pass

class Cat(Animal):
    def __init__(self,name,animal_type,shape,nature):
        super().__init__(animal_type,shape,nature)
        self.name = name
        if super().fierce_animal:
            self.suitable_for_pet = False
        else:
            self.suitable_for_pet = True
        self.say_someting = "miao miao miao"

    
    def animal_call(self):
        print(self.say_someting)

class Dog(Animal):
    def __init__(self,name,animal_type,shape,nature):
        super().__init__(animal_type,shape,nature)
        self.name = name
        if super.fierce_animal:
            self.suitable_for_pet = False
        else:
            self.suitable_for_pet = True
        self.say_someting = "wang wang wang"


    def animal_call(self):
        print(self.say_someting)

class Zoo:
    def __init__(self,name):
        self.name = name
        self.animal = {}
    def add_animal(self,object):
        pass



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
