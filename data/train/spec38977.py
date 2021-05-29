import numpy as np 

def function(x):

	v2 = 1
	e3 = x
	paths = []
	try:
		if v2 >= 4:
			x = 1*x
			v2 = v2*8
			v2 = v2-x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x > 5:
			x = e3+e3
			paths.append(3)
		else:
			x = 0+e3
			e3 = 3+e3
			v2 = v2*1
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