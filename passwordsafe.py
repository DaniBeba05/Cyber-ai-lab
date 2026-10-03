import module

p = module.Password("", 0)

while p.comprobar_num_intentos():

    p.introducirpassword()

    try:
        p.comprobar_password_valida()
        print(p.mensajedepasswordvalida())
        break

    except (module.TienelongitudmaximaError,
            module.TienemayusculaError,
            module.TienenumeroError,
            module.TieneunsimboloError) as error:
        
        print(error)
        p.sumar_num_intentos()

        if not p.comprobar_num_intentos():
            print(p.mensajedesuperaciondeintentos())