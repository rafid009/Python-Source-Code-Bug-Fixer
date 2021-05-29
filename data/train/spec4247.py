import numpy as np 

def function(x):

	v0 = x
	j2 = x
	paths = []
	try:
		if j2 > 0:
			j2 = 1*5
			x = v0-8
			paths.append(1)
		else:
			x = 2*x
			v0 = v0+v0
			v0 = x+v0
			paths.append(2)
		if j2 < 5:
			j2 = 3+j2
			v0 = 3+8
			paths.append(3)
		else:
			x = 0+x
			x = 9+3
			x = 5+j2
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