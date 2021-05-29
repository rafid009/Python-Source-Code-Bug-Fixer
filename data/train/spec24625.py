import numpy as np 

def function(x):

	v1 = 6
	d5 = 9
	paths = []
	try:
		if d5 < 2:
			x = x*x
			v1 = 4-v1
			v1 = 1+v1
			paths.append(1)
		else:
			x = 1+x
			v1 = 3+v1
			paths.append(2)
		if x >= 4:
			v1 = 8-v1
			x = v1*3
			x = x+x
			paths.append(3)
		else:
			d5 = d5+5
			x = v1/x
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