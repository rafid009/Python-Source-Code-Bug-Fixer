import numpy as np 

def function(x):

	v1 = x
	t9 = x
	paths = []
	try:
		if v1 > 9:
			x = x/7
			paths.append(1)
		else:
			v1 = v1-7
			x = x+3
			v1 = v1-8
			paths.append(2)
		if v1 >= 0:
			x = 3*1
			v1 = v1*t9
			paths.append(3)
		else:
			v1 = v1-5
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