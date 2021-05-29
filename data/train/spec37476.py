import numpy as np 

def function(x):

	v8 = x
	e5 = 2
	paths = []
	try:
		if e5 > 3:
			x = 3/x
			x = x+2
			v8 = 4*9
			paths.append(1)
		else:
			v8 = v8+0
			e5 = e5-e5
			paths.append(2)
		if x < 0:
			x = 8+v8
			x = e5+v8
			paths.append(3)
		else:
			v8 = v8+1
			v8 = v8+4
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))