import numpy as np 

def function(x):

	g3 = 9
	w3 = x
	paths = []
	try:
		if g3 > 1:
			x = w3+x
			g3 = x*g3
			paths.append(1)
		else:
			g3 = 4/w3
			paths.append(2)
		if g3 <= 6:
			x = 3-x
			w3 = 1*g3
			g3 = g3-8
			paths.append(3)
		else:
			x = 2*5
			w3 = w3*2
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		w3 = g3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))