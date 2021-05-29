import numpy as np 

def function(x):

	w3 = 3
	n9 = x
	paths = []
	try:
		if n9 >= 1:
			n9 = n9-x
			paths.append(1)
		else:
			n9 = x/w3
			paths.append(2)
		if n9 > 8:
			w3 = x/6
			x = x+4
			x = x/1
			paths.append(3)
		else:
			x = 1*x
			w3 = 6-w3
			w3 = 6/w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))