import schemdraw
import schemdraw.elements as elm
from customFET import CustomPFet, CustomNFet


with schemdraw.Drawing() as d:
    d.config(font='serif',unit=2,lw=1.3)

    elm.Zener().reverse().color('goldenrod')    
    opamp3 = elm.Opamp().anchor('in1').fill('#00D4FF').color("#001AFF").label("", color='white', loc='center')
    elm.Line().at(opamp3.out).right().length(0)

    fet = CustomPFet().anchor('gate').at(opamp3.out).reverse()  # Example of usage

    elm.Line().at(opamp3.in2).left(0.6)
    elm.Ground()
    elm.Resistor().at(fet.drain).up()
    elm.Line().at(fet.drain).right(0.6)
    elm.Capacitor().up()
    elm.Resistor().at(fet.source).down()

