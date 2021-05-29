import numpy as np 

def function(x):

	n1 = x
	v0 = 9
	paths = []
	try:
		if n1 < 8:
			v0 = n1+7
			n1 = 2-n1
			v0 = x+v0
			paths.append(1)
		else:
			v0 = v0+9
			paths.append(2)
		if x < 8:
			v0 = n1/2
			v0 = n1-2
			paths.append(3)
		else:
			n1 = n1+2
			n1 = n1-2
			n1 = n1-x
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