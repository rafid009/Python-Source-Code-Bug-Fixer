import numpy as np 

def function(x):

	w6 = x
	v3 = x
	paths = []
	try:
		if w6 > 7:
			v3 = v3*x
			paths.append(1)
		else:
			v3 = 6-w6
			v3 = v3+5
			w6 = x-x
			paths.append(2)
		if w6 >= 6:
			v3 = 9+v3
			w6 = w6+x
			v3 = 5/6
			paths.append(3)
		else:
			x = 3+x
			v3 = 2*v3
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