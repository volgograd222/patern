class lights:

    def use(self):
        print("use lights")


class Engine:

    def on(self):
        print("engine on")


class Climat:

    def control(self):
        print("climat control")


class Music:

    def turn(self):
        print("music turn")


class CarFacade:

    def __init__(self):
        self._engine = Engine()
        self._climat = Climat()
        self._music = Music()
        self._lights = lights()
    def engineon(self):
        self._engine.on()

    def climatcontrol(self):
        self._climat.control()

    def musicturn(self):
        self._music.turn()

    def lightsuse(self):
        self._lights.use()


if __name__ == '__main__':
    facade = CarFacade()
    facade.climatcontrol()
    facade.musicturn()
    facade.engineon()
    facade.lightsuse()
