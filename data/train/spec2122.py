import numpy as np 

def function(x):

	y8 = 1
	w3 = 6
	paths = []
	try:
		if y8 > 7:
			w3 = 6+w3
			x = x-x
			paths.append(1)
		else:
			y8 = 3/w3
			w3 = 5-6
			y8 = y8+7
			paths.append(2)
		if y8 > 6:
			y8 = y8*9
			w3 = 8+2
			w3 = 9+w3
			paths.append(3)
		else:
			x = 1+x
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