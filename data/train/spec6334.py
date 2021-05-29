import numpy as np 

def function(x):

	v2 = 9
	n3 = x
	paths = []
	try:
		if v2 < 6:
			v2 = 7/8
			v2 = v2*v2
			paths.append(1)
		else:
			n3 = n3*v2
			paths.append(2)
		if x >= 3:
			v2 = v2+v2
			v2 = 8-3
			paths.append(3)
		else:
			n3 = 1-n3
			v2 = x*v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))