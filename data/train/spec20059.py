import numpy as np 

def function(x):

	b2 = 5
	w3 = x
	paths = []
	try:
		if w3 >= 3:
			w3 = w3+w3
			w3 = w3*1
			paths.append(1)
		else:
			w3 = x+x
			w3 = 5*x
			paths.append(2)
		if x >= 7:
			b2 = 1*x
			w3 = w3*x
			paths.append(3)
		else:
			w3 = 8-w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))