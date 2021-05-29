import numpy as np 

def function(x):

	v8 = 7
	p2 = x
	x = x
	paths = []
	try:
		if x <= 2:
			v8 = 5-v8
			paths.append(1)
		else:
			x = v8+v8
			v8 = 5*v8
			paths.append(2)
		if x >= 3:
			v8 = v8*v8
			v8 = 7/9
			paths.append(3)
		else:
			x = x+2
			v8 = 9-v8
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