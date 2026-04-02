from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        """This has to be implemented by specific class"""
        pass

    def main_operation(self):
        """Here we create a product and implement the main logic"""
        product = self.factory_method()
        product.operation()
        # Some other logic


class Product(ABC):
    @abstractmethod
    def operation():
        """This has to be implemented by specific class"""
        pass


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class ConcreteProduct1(Product):
    def operation(self):
        print("Operation of the concrete product 1")


class ConcreteProduct2(Product):
    def operation(self):
        print("Operation of the concrete product 2")


def client(creator: Creator):
    """Client code"""
    creator.main_operation()


if __name__ == "__main__":
    client(ConcreteCreator1())
    client(ConcreteCreator2())
