import numpy as np 

def function(x):

	v0 = 5
	w5 = 1
	paths = []
	try:
		if v0 < 9:
			v0 = v0+3
			paths.append(1)
		else:
			w5 = x+w5
			x = 2*7
			paths.append(2)
		if v0 >= 7:
			w5 = w5-x
			v0 = v0*4
			paths.append(3)
		else:
			w5 = w5-4
			v0 = v0*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))