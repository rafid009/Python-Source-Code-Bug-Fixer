import numpy as np 

def function(x):

	n3 = 6
	v7 = x
	paths = []
	try:
		if v7 >= 5:
			v7 = n3*v7
			n3 = 1-n3
			x = n3-x
			paths.append(1)
		else:
			x = n3*7
			n3 = v7-n3
			paths.append(2)
		if v7 < 2:
			x = 2*x
			paths.append(3)
		else:
			x = 1*x
			v7 = 6+v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))