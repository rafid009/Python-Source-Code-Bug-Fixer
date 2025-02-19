import numpy as np 

def function(x):

	b6 = 2
	w7 = x
	paths = []
	try:
		if x <= 4:
			b6 = 4/8
			w7 = b6+w7
			paths.append(1)
		else:
			w7 = w7-9
			b6 = 9+b6
			x = x+4
			paths.append(2)
		if x < 8:
			b6 = b6*2
			w7 = b6*x
			paths.append(3)
		else:
			x = 1-x
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