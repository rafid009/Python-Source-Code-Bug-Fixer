import numpy as np 

def function(x):

	x9 = 2
	v8 = 3
	paths = []
	try:
		if x9 > 6:
			v8 = x9*x9
			paths.append(1)
		else:
			v8 = 4*v8
			paths.append(2)
		if v8 < 9:
			x9 = 6*x9
			v8 = v8*x
			paths.append(3)
		else:
			v8 = 5+v8
			x = x*2
			x9 = 4+x9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))