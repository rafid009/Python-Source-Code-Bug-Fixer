import numpy as np 

def function(x):

	a5 = x
	w3 = x
	paths = []
	try:
		if a5 <= 3:
			w3 = 6+w3
			paths.append(1)
		else:
			x = x-a5
			paths.append(2)
		if a5 <= 8:
			x = x+x
			a5 = 7/7
			paths.append(3)
		else:
			a5 = a5+x
			x = x+4
			a5 = 0/a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))