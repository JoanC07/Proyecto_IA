
import  unittest 

from BFS import grafo_

class check(unittest.TestCase):
    
    def prueba_grafo(self):
        grafo = grafo_(1, 6)
        
        self.assertEqual(grafo ,[1, 0, 2, 6])
        
if __name__ == "__main__":
    unittest.main()
           
    