'''Librería servo.'''
from machine import Pin, PWM

class Servo:

    def __init__(self, pwm_pin:int, min_pulse_ms:float = 0.5, max_pulse_ms:float = 2.4, frequency:int = 50) -> None:
        '''Una clase para el Servo motor.\n
           Args:
                pwm_pin: El pin de la señal PWM.
                min_pulse: El pulso mínimo en milisegundos.
                max_pulse: El pulso máximo en milisegundos.
                frequency: La frecuencia en Hz.'''
        self.__servo = PWM(Pin(pwm_pin), freq = frequency)
        self.__min_pulse_ns = min_pulse_ms * 1_000_000
        self.__max_pulse_ns = max_pulse_ms * 1_000_000
        self.__pulse_width = 0
        self.__current_degrees = 0

    def rotate(self, degrees:int) -> None:
        '''Mueve el servo a los grados deseados (0-180°).'''
        if degrees < 0 or degrees > 180:
            raise ValueError("Sólo ángulos con rango de 0 a 180.")
        self.__current_degrees = degrees
        pulse_width = int(self.__min_pulse_ns + (degrees / 180) * (self.__max_pulse_ns - self.__min_pulse_ns))
        self.__servo.duty_ns(pulse_width)
        self.__pulse_width = pulse_width
    
    def set_min_pulse_ms(self, min_pulse_ms:float) -> None:
        '''
        :param min_pulse_ms: El pulso mínimo en milisegundos.
        :type min_pulse_ms: float
        '''
        self.__min_pulse_ns = min_pulse_ms * 1_000_000

    def set_max_pulse_ms(self, max_pulse_ms:float) -> None:
        '''
        :param max_pulse_ms: El pulso máximo en milisegundos.
        :type max_pulse_ms: float
        '''
        self.__max_pulse_ns = max_pulse_ms * 1_000_000

    def get_min_pulse_ns(self) -> float:
        '''Retorna el pulso mínimo en nanosegundos.'''
        return self.__min_pulse_ns
    
    def get_max_pulse_ns(self) -> float:
        '''Retorna el pulso máximo en nanosegundos.'''
        return self.__max_pulse_ns
    
    def get_pulse_width(self) -> float:
        '''Retorna el ancho de pulso actual en milisegundos.'''
        return self.__pulse_width / 1_000_000
    
    def get_current_degrees(self) -> int:
        '''Retorna los grados actuales del servo.'''
        return self.__current_degrees
        
if __name__ == '__main__':
    servo = Servo(pwm_pin = 0, min_pulse_ms = 0.5, max_pulse_ms = 2.4, frequency = 50)
    from time import sleep

    try:
        while True:
            for degree in [0, 45, 90, 135, 180]:
                servo.rotate(degree)
                print(servo.get_pulse_width())
                sleep(1)

    except KeyboardInterrupt:
        servo.rotate(0)
