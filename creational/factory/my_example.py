from abc import ABC, abstractmethod


class Phone(ABC):
    @abstractmethod
    def call(self, phone_number: int):
        pass


class Tablet(ABC):
    @abstractmethod
    def play_video(self, file_name: str):
        pass


class Watch(ABC):
    @abstractmethod
    def connect_to_phone(self, phone: Phone):
        pass

    @abstractmethod
    def connect_to_tablet(self, tablet: Tablet):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_phone(self) -> Phone:
        pass

    @abstractmethod
    def create_tablet(self) -> Tablet:
        pass

    @abstractmethod
    def create_watch(self) -> Watch:
        pass

    def create_products(self) -> (Phone, Tablet, Watch):
        return self.create_phone(), self.create_tablet(), self.create_watch()


class Iphone(Phone):
    def call(self, phone_number: int):
        print(f"Calling from Iphone to {phone_number} ...")


class Ipad(Tablet):
    def play_video(self, file_name: str):
        print(f"Playing video from Ipad {file_name} ...")


class AppleWatch(Watch):
    def connect_to_phone(self, phone: Phone):
        if isinstance(phone, Iphone):
            print("Connecting to phone ...")
        else:
            print("Cannot connect, phone must be Apple")

    def connect_to_tablet(self, tablet: Tablet):
        if isinstance(tablet, Ipad):
            print("Connecting to tablet ...")
        else:
            print("Cannot connect, tablet must be Apple")


class AppleFactory(AbstractFactory):
    def create_phone(self) -> Phone:
        return Iphone()

    def create_tablet(self) -> Tablet:
        return Ipad()

    def create_watch(self) -> Watch:
        return AppleWatch()


class Galaxy(Phone):
    def call(self, phone_number: int):
        print(f"Calling from Galaxy to {phone_number} ...")


class SamsungTablet(Tablet):
    def play_video(self, file_name: str):
        print(f"Playing video from Samsung Tablet {file_name} ...")


class GalaxyWatch(Watch):
    def connect_to_phone(self, phone: Phone):
        if isinstance(phone, Galaxy):
            print("Connecting to phone ...")
        else:
            print("Cannot connect, phone must be Samsung")

    def connect_to_tablet(self, tablet: Tablet):
        if isinstance(tablet, SamsungTablet):
            print("Connecting to tablet ...")
        else:
            print("Cannot connect, tablet must be Samsung")


class SamsungFactory(AbstractFactory):
    def create_phone(self) -> Phone:
        return Galaxy()

    def create_tablet(self) -> Tablet:
        return SamsungTablet()

    def create_watch(self) -> Watch:
        return GalaxyWatch()


def client(factory: AbstractFactory):
    phone, tablet, watch = factory.create_products()
    phone.call(1234)
    tablet.play_video("my_video.mp4")
    watch.connect_to_phone(phone)
    watch.connect_to_tablet(tablet)


if __name__ == "__main__":
    print("=== Apple client ===")
    client(AppleFactory())
    print("=== Samsung client ===")
    client(SamsungFactory())
