import numpy as np 

def function(x):

	v3 = x
	d4 = x
	paths = []
	try:
		if x > 3:
			x = 7/9
			d4 = 9/d4
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if x >= 3:
			v3 = 6+v3
			paths.append(3)
		else:
			v3 = 4-v3
			x = 5*x
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		v3 = d4**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))