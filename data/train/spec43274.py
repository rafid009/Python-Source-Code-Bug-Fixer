import numpy as np 

def function(x):

	o6 = 8
	w5 = 5
	paths = []
	try:
		if w5 > 0:
			o6 = o6+4
			paths.append(1)
		else:
			o6 = o6*3
			paths.append(2)
		if w5 < 5:
			x = x*x
			paths.append(3)
		else:
			o6 = x-o6
			o6 = 8*1
			w5 = w5+5
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