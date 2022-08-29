# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть унаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport

# экземпляр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключений


from abc import ABC, abstractmethod


class Transport(ABC):
	@abstractmethod
	def start_engine(self):
		pass

	@abstractmethod
	def stop_engine(self):
		pass

	@abstractmethod
	def move(self):
		pass

	@abstractmethod
	def stop(self):
		pass


class Boat(Transport):
	def start_engine(self):
		print("Engine started")

	def stop_engine(self):
		print("Engine was broke!")

	def move(self):
		print("Boat is swim in the sea")

	def stop(self):
		print("Boat stopped at the pier")


class Car(Transport):
	def start_engine(self):
		print("Engine is fire-up")

	def stop_engine(self):
		print("Engine exploded =(!")

	def move(self):
		print("Car pull out of the street")

	def stop(self):
		print("Car stopped in the garage")


class Electroscooter(Transport):
	def start_engine(self):
		print("Electroscooter has flashed the LED")

	def stop_engine(self):
		print("Electroscooter has flashed the LED twice")

	def move(self):
		print("The Electroscooter's speed on the street is very high")

	def stop(self):
		print("The Electroscooter's driver is falling into the swimming pool")


class Person:
	def use_transport(self, transport: Transport):
		transport.start_engine()
		transport.stop_engine()
		transport.move()
		transport.stop()


# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
	boat = Boat()
	car = Car()
	kamikadze = Electroscooter()

	person = Person()
	person.use_transport(boat)
	print('=' * 10)
	person.use_transport(car)
	print('=' * 10)
	person.use_transport(kamikadze)
