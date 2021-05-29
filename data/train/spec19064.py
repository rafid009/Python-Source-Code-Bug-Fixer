import numpy as np 

def function(x):

	v3 = x
	b5 = 7
	paths = []
	try:
		if v3 >= 1:
			v3 = 4*b5
			paths.append(1)
		else:
			b5 = 9-b5
			paths.append(2)
		if v3 >= 3:
			b5 = b5*6
			v3 = 5*v3
			paths.append(3)
		else:
			b5 = 3*b5
			x = x*4
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))