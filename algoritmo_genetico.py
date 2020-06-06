'''Se importa la libreria random para crear o generar numeros o nodos aleatorios'''
import random

'''se crea una clase para la representacion de un nodo'''
class Nodo(object):

'''Se define el constructor, donde cada nodo tendra 
	un nombre y una cordenada x y y', y se crea la copia de un nodo'''
	def_init_(self, Nombre = "", X = 0, Y = 0, Nodo = None):

'''Esta linea de codigo representa una condicion en donde 
   si nodo es nada o esta vacio'''
	if Nodo is None:
		'''Nombre del nodo va ser igual a la variable nombre''' 
		self.Nombre = Nombre
		'''la cordenada x va ser igual a lo que valga la variable x'''
		self.X = X
		'''la cordenada y va ser igual a lo que valga el parametro y'''
		self.Y = Y
	'''el else se activa cuando nodo sea diferente de none, se pasa un nodo como argumento'''
	else:
		'''se crea una copia a partir de este nodo que se pasa como argumento
			donde Nombre del nodo va ser igual a otro nodo que se pasa como argumento '''
		self.Nombre = Nodo.Nombre
		'''en esta linea representa x va ser igual a otra cordenada de x'''
		self.X = Nodo.X
		'''en esta linea representa y va ser igual a otra cordenada de y'''
		self.Y = Nodo.Y
	'''esta linea representa que todo nodo creado tendra un padre
		y va ser none al momento de inicializarse'''
	self.Padre = None

'''Se genera una funcion donde genera 
	tantos arboles como nodos haya, tiene dos variables nNodos
	y la distancia que existe entre cada nodo'''
def GenerarPoblacion(nNodos, distancia):
	
	'''la variable rango tendra un valor sacandolo
		con la siguiente formula 10 elevado al valor de la potencia -1
		es de'''
	rango = 10 ** distancia - 1

	'''variable donde se crea una lista de nodos'''
	nodos = []

	'''variable donde se crean las posibles rutas del viajero'''
	poblacion = []

'Se crea cada uno de los nodos utilizando la condicion for'

	''' condicion que se va a iterar dependiendo de la cantidad de nodos 
		i va a tomar un valor desde 0
		si nNodos vale 5 entonces i se va a generar de 0 hasta 4 '''
	for i in range(nNodos):

		'''se obtiene el nombre de un nodo y seria igual a i + 1 
			suponiendo que vale 5 entonces seria  de 0 a 4 y el 
			mas uno contaria de 1 hasta 5 '''
		nombre = i + 1
		
		'''se calcula cordenada x y se manda a llamar la funcion randint 
			donde se crea numeros aleatorios especficando el rango que va a ser,
			especificando tanto numeros positivos como numeros negativos 
			si el rango es de 9, seria de -9 a 9 '''	
		x = random.randint(-rango, rango)

		'''se calcula cordenada "y" y se manda a llamar la funcion randint 
			donde se crea numeros aleatorios especficando el rango que va a ser,
			especificando tanto numeros positivos como numeros negativos 
			si el rango es de 9, seria de -9 a 9 '''
		y = random.randint(-rango, rango)

		'''Se crea el nodo donde se manda a llamar el constructor
			que es def_init_(self, Nombre = "", X = 0, Y = 0, Nodo = None):
			donde Nombre va a ser igual a nombre, y x,y tomaran un valor aleatorio
			el parametro de Nodo seguira tomando un valor de none el la instruccion
			mandando a llamar la funcion:
			else:
			self.Nombre = Nodo.Nombre
			self.X = Nodo.X
			self.Y = Nodo.Y
			self.Padre = None
			   '''
		nodo = Nodo(Nombre = nombre, X = x, Y = y)

		'''nodo se agrega a la lista de nodos'''
		nodos.append(nodo)

		'''se crean arboles como nodos hayya en la listta de nodos'''
	for nodo in nodos:
		
		'''se crean los nodos por visitar donde se obtienen
		de una copia de la lista de nodos'''
		nodosPorVisitar = nodos[:]
		
		'''nodos por visitar se remueven al nodo que pertenece esa iteracion'''
		nodosPorVisitar.remove(nodo)
		
		'''se manda allamar la funcion generar arbol
			y se le pasa la raiz dependiendo de la iteracion se van generando los nodos'''
		GenerarArbol(nodo, nodosPorVisitar, poblacion)

	'''se devuelve la poblacion'''
	return poblacion


'''funcion en donde se generan los arboles
	donde tendra los parametros de nodos, 
	nodos por visitar y la poblacion que se va a utilizar'''	
def GenerarArbol(raiz, nodosPorVisitar, poblacion):
	
	'''funcion que dejara de ejecutarse cuando no haya mas nodos por visitar'''
	if len(nodosPorVisitar) > 0:

		'''por cada nodo por visitar se realizaran las funciones siguientes'''
		for nodo in nodosPorVisitar:

			'''nodos faltantes va a ser igual a toda la lista de nodos por visitar
			 '''
			nodosFaltantes = nodosPorVisitar[:]

			''' a la copia de nodos faltantes se va aremover el nodo donde se va a mandar 
			a llamar la funcion de generar arbol'''
			nodosFaltantes.remove(nodo)

			'''se crea una copia del nodo donde nodo es igual a nodo
			   esta funcion  hijo = Nodo(Nodo = nodo) 
			   va a llamar al constructor 
			   (self, Nombre = "", X = 0, Y = 0, Nodo = None)
			'''
			hijo = Nodo(Nodo = nodo)

			'''el padre de este nodo va a ser igual a nodo'''
			hijo.Padre = raiz

			'''se llama la funcion generar arbol donde se va a psar el nodo hijo 
			los nodos faltantes y la poblacion donde se va insertar cada una de las posibles rutas
			esto sera recursivo'''
			GenerarArbol(hijo, nodosFaltantes, poblacion)
		
		'''caundo ya no haya nodos por visitar se encuentra la siguiente funcion'''
		else:

			'''n sera igual a raiz'''
			n = raiz

			'''se crea una lista de solucion donde todos los nodos
			se almacenaran se obtiene una sola lista de solucion'''
			solucion = []

			'''se crea un ciclo while donde n no este vacio'''
			while n is not None:

				'''mientras que la solucion se le agreaga el nodo  '''
				solucion.append(n)
				
				'''y n va a ser igual a al padre de n, es decir va
				a subir de nodo
				n va air escalando el arvol asi llega en un punto donde no 
				tiene padre y asi se obtien el listado de la solucion'''
				n = n.Padre

			'''la solucion quedo inversa, es decir que se estaria escalando
			de manera inversa de manera ordenada 12345'''	
			solucion.reverse()

			'''agrega la solucion a la poblacion '''
			poblacion.append(solucion)

'''se manda a llamar la funcion main '''
if _name_ == "_main_"

	'''se crea la varible nNodos para pedir el numero de nodos que se van a generar'''
	nNodos = int(input('Ingrese cantidad de nodos: '))

	'''se crea la variable distancia para que pida el valor de la distancia'''
	distancia = int (input('Ingrese valor de distancia: '))

	'''se pasan con parametros y se devuelve la poblacion'''
	poblacion = GenerarPoblacion(nNodos, distancia)
	
	'''por cada una de las soluciones que esten dentro de la poblacion
	se uniran es deir se imprimen'''
	for solucion in poblacion:
		
		'''se crea una variable string para unir las soluciones'''
		string = "["

		'''por cada uno de los nodos de una solucion se concatenan'''
		for nodo in solucion:

			'''dentro de la variables string se concatenan
			las posibles soluciones generadas teniendo un rango '''
			string = string + str(nodo.Nombre) + " "

		'''se imrime la variable strin que contiene las soluciones'''
		print string + "]"


		'''Esta funcion permite calcular las cordenadas de cada nodo'''
		for nodo in poblacion[0]:

			'''se imprime el numero de nodo y se concatena la cordenada de "x y "y "'''
			print str(nodo.Nombre) + " X =" + str(nodo.X) + " Y =" + str(nodo.Y)

