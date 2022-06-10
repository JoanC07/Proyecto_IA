

import  unittest 

from BFS import graph_

from agente import Search
# dicionarios para evaluar la funcion search 
objetivo = {'Gallinas': '0',
 'Perros': '0', 
 'Cerdos': '0',
 'Burros': '0',
 'Chivos': '0', 
 'Vacas': '0',
 'Conejos':'0',
 'Patos': '0',
 'Ovejas': '0' } 


class check(unittest.TestCase):
    
        
    def test_agent(self):
        g = Search(objetivo)
        self.assertEqual(g ,18)
        
        

if __name__ == "__main__":
    unittest.main()
    