from gpiozero import DistanceSensor, Servo,  AngularServo



class Robot:
    
    
    
    def __init__(self, gpio_esteira1, gpio_esteira2, gpio_garra):

        self.gpio_esteira1 = gpio_esteira1
        self.gpio_esteira2 = gpio_esteira2
        self.gpio_garra = gpio_garra
        
        self.servo_1 = Servo(gpio_esteira1)
        self.servo_2 = Servo(gpio_esteira2)
        self.garra = AngularServo(gpio_garra, min_angle=-90, max_angle=90)


    def movienta_frente(self, gpio_esteira1, gpio_esteira2):

        self.servo_1.min()
        self.servo_2.min()


    def movienta_tras(self, gpio_esteira1, gpio_esteira2):

        self.servo_1.min()
        self.servo_2.min()       


    def movienta_esquerda(self, gpio_esteira2):

        self.servo_2.min()


    def movienta_direita(self,gpio_esteira1):
       
        self.servo_1.min()


    def movienta_garra_abre(self, gpio_garra):

        self.garra.angle = -90


    def movienta_garra_fecha(self, gpio_garra):
        
        self.garra.angle = 90
