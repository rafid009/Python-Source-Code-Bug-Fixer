import numpy as np 

def function(x):

	n0 = 4
	v9 = 2
	paths = []
	try:
		if n0 <= 2:
			x = v9+4
			n0 = n0+4
			v9 = 7-v9
			paths.append(1)
		else:
			n0 = x/4
			v9 = 9*4
			paths.append(2)
		if v9 > 4:
			n0 = n0+x
			v9 = 1+v9
			paths.append(3)
		else:
			v9 = 6+v9
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))