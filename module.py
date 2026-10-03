class IntentosSuperadosError(Exception):
    pass


class TienelongitudmaximaError(Exception):
    pass


class TienemayusculaError(Exception):
    pass


class TienenumeroError(Exception):
    pass


class TieneunsimboloError (Exception):
    pass 
                          

class Password: 

    def __init__(self, contraseña, num_intentos, intentos_maximos = 3, minimo = 12):
        self.contraseña = contraseña
        self.num_intentos = num_intentos
        self.intentos_maximos = intentos_maximos
        self.minimo = minimo


    def introducirpassword(self):
    
        self.contraseña = str (input("Password:"))
    
        return self.contraseña

    def tiene_longitud_maxima(self):
        if len(self.contraseña) < self.minimo:

            raise TienelongitudmaximaError(self.mensajerequisitonumcaracteres())
        
        return True


    def tiene_una_mayuscula(self):
        if not any(caracter.isupper() for caracter in self.contraseña):

            raise TienemayusculaError(self.mensajerequisitomayuscula())
        
        return True


    def tiene_un_numero(self):
        if not any(caracter.isdigit() for caracter in self.contraseña):

            raise TienenumeroError(self.mensajerequisitonumero())
        
        return True


    def tiene_un_simbolo(self):
        simbolos = '.,@#?!>;:-_'
        if not any(caracter in simbolos for caracter in self.contraseña):

            raise TieneunsimboloError(self.mensajerequisitosimbolo())
        
        return True

    

    def comprobar_num_intentos(self):

        return self.num_intentos < self.intentos_maximos


    def sumar_num_intentos (self):

        self.num_intentos+=1


    
    def comprobar_password_valida(self):
        self.tiene_longitud_maxima()
        self.tiene_una_mayuscula()
        self.tiene_un_numero()
        self.tiene_un_simbolo()

        return True

    def mensajedepasswordvalida(self):
         
        return "La contraseña introducida es valida"

    
    def mensajedesuperaciondeintentos(self):

        return "Has superado el número de intentos posibles. Vuelve a intentarlo más tarde"



    def mensajerequisitomayuscula(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos una mayúscula"



    def mensajerequisitonumero(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos un número"



    def mensajerequisitosimbolo(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos un simbolo"



    def mensajerequisitonumcaracteres(self):

        return "Compruebe si su contraseña cumple los requisitos de tener al menos 12 carácteres"


    