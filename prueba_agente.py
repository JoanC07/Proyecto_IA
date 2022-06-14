
'''
Importacion de librerias para prueba unitarias
de archivo py correspondiente al agente
Crea dicionarios para evaluar la funcion Buscar
'''
import  unittest 
from agente import Buscar, verificar_existencia
# 
objetivo = {'Gallinas': '0',
 'Perros': '0', 
 'Cerdos': '0',
 'Burros': '0',
 'Chivos': '0', 
 'Vacas': '0',
 'Conejos':'0',
 'Patos': '0',
 'Ovejas': '0' } 
objetivo_1 = {}
class prueba(unittest.TestCase):
    '''Clase prueba 
    Procedimiento test_agente
        instanciamos la funcion que se va evaluar
        con la funcion de unittest(parametros para evaluar)
    Procedimiento test_costo_0
        instanciamos la funcion que se va evaluar
        Se le añaden parametro de evaluacion y verifica
    '''   
    def test_agente(self):#procedimeinto para realizar el test del agente con la medida de optimizacion
        g = Buscar(objetivo)#instancia la funcción a evaluar
        self.assertEqual(g ,17)#indica los parametros que van a evaluar

    def test_costo_0(self):# procedimiento para Test diccionario vacio
        t = verificar_existencia(objetivo_1)#instancia la funcción a evaluarP
        self.assertEqual(t, 'Diccionario vacio')#indica los parametros que van a evalua
        
    def test_estado(self):
        g= Buscar(objetivo)
        self.assertEqual(g,1)
if __name__ == "__main__":
    unittest.main()
    