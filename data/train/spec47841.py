import numpy as np 

def function(x):

	v4 = x
	e4 = 1
	x = x
	paths = []
	try:
		if v4 <= 4:
			x = 8*e4
			e4 = v4+e4
			e4 = e4*e4
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if e4 >= 4:
			v4 = 9/v4
			x = 7-5
			paths.append(3)
		else:
			e4 = 6*e4
			x = e4-4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))