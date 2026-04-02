from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """This class groups creation of many products that belong to one "family" of products."""

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

    def create_products(self):
        product_a = self.create_product_a()
        product_b = self.create_product_b()

        product_b.colloborate(product_a)


class ProductA(ABC):
    @abstractmethod
    def operation(self):
        pass


class ProductB(ABC):
    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def colloborate(self, product_a: ProductA):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB2()


class ConcreteProductA1(ProductA):
    def operation(self):
        print("Concrete product A1 operation")


class ConcreteProductA2(ProductA):
    def operation(self):
        print("Concrete product A2 operation")


class ConcreteProductB1(ProductB):
    def operation(self):
        print("Concrete product B1 operation")

    def colloborate(self, product_a: ProductA):
        """Even though concrete product can colloborate only with another product from the same family, the typing should specify the abstract class"""
        product_a.operation()
        self.operation()


class ConcreteProductB2(ProductB):
    def operation(self):
        print("Concrete product B2 operation")

    def colloborate(self, product_a: ProductA):
        """Even though concrete product can colloborate only with another product from the same family, the typing should specify the abstract class"""
        product_a.operation()
        self.operation()


def client(factory: AbstractFactory):
    factory.create_products()


if __name__ == "__main__":
    client(ConcreteFactory1())
    client(ConcreteFactory2())
