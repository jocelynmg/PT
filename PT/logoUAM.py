from color import Color

c = Color()

def printLogo():
    """Regresa el encabezado de la aplicación"""

    logo = """
    """ + c.RED + """##########################################################################""" + c.END + """
    """ + c.RED + """#                                                                        #""" + c.END + """
    """ + c.RED + """#                               ╦ ╦╔═╗╔╦╗                                #""" + c.END + """
    """ + c.RED + """#                               ║ ║╠═╣║║║                                #""" + c.END + """
    """ + c.RED + """#                               ╚═╝╩ ╩╩ ╩                                #""" + c.END + """
    """ + c.RED + """#                   ┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌┬┐┌─┐┌─┐┬  ┌─┐┌─┐                 #""" + c.END + """
    """ + c.RED + """#                   ├─┤┌─┘│  ├─┤├─┘│ │ │ ┌─┘├─┤│  │  │ │                 #""" + c.END + """
    """ + c.RED + """#                   ┴ ┴└─┘└─┘┴ ┴┴  └─┘ ┴ └─┘┴ ┴┴─┘└─┘└─┘                 #""" + c.END + """
    """ + c.RED + """#                                                                        #""" + c.END + """
    """ + c.RED + """# ====================================================================== #""" + c.END + """
    """ + c.RED + """#""" + c.END + """                                                                        """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """  """ + c.BOLD + c.YELLOW + """PROYECTO TERMINAL PARA LA CAPACITACIÓN Y DESARROLLO DE HABILIDADES""" + c.END + """    """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """  """ + c.BOLD + c.YELLOW + """EN LA TECNOLOGÍA DE DOCKER""" + c.END + """                                            """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """                                                                        """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """  """ + c.BOLD +"""ALUMNA: JOCELYN MENDOZA GONZÁLEZ""" + c.END + """                                      """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """  """ + c.BOLD +"""PROFESOR: HUGO PABLO LEYVA""" + c.END + """                                            """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """                                                                        """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """  """ + c.BOLD +"""SISTEMA OPERATIVO: CentOS 8""" + c.END + """                                           """ + c.RED + """#""" + c.END + """
    """ + c.RED + """#""" + c.END + """                                                                        """ + c.RED + """#""" + c.END + """
    """ + c.RED + """##########################################################################""" + c.END + """
    """
    
    return logo


