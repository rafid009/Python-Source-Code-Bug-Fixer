import numpy as np 

def function(x):

	o1 = x
	w3 = x
	paths = []
	try:
		if o1 <= 3:
			o1 = 2*o1
			o1 = 7-o1
			paths.append(1)
		else:
			w3 = w3+6
			o1 = 9-2
			paths.append(2)
		if x < 0:
			w3 = w3-8
			w3 = w3+0
			paths.append(3)
		else:
			x = x+w3
			w3 = 2*4
			x = w3/1
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