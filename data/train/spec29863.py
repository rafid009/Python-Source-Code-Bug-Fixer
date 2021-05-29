import numpy as np 

def function(x):

	v8 = x
	e4 = 8
	paths = []
	try:
		if e4 >= 7:
			e4 = x+e4
			x = v8*x
			e4 = 8-x
			paths.append(1)
		else:
			e4 = 7*v8
			paths.append(2)
		if v8 < 5:
			v8 = 2-4
			paths.append(3)
		else:
			e4 = e4+e4
			x = v8*x
			v8 = v8*v8
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		v8 = e4**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))