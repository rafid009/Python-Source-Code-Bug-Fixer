import numpy as np 

def function(x):

	v6 = x
	d8 = 7
	paths = []
	try:
		if x >= 1:
			v6 = v6+4
			paths.append(1)
		else:
			v6 = x-v6
			d8 = d8*9
			v6 = 8*v6
			paths.append(2)
		if x < 3:
			v6 = v6-2
			paths.append(3)
		else:
			v6 = 8*v6
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))