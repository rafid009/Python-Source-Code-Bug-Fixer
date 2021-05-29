import numpy as np 

def function(x):

	w6 = 8
	g1 = 1
	paths = []
	try:
		if w6 < 2:
			x = x/8
			x = 1/g1
			g1 = x+2
			paths.append(1)
		else:
			w6 = w6/6
			w6 = 4-6
			w6 = w6+9
			paths.append(2)
		if w6 >= 2:
			x = x/8
			w6 = 2+1
			paths.append(3)
		else:
			x = g1+x
			g1 = x*7
			w6 = w6/w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))