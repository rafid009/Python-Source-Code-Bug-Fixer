import numpy as np 

def function(x):

	v6 = 0
	d0 = 1
	paths = []
	try:
		if d0 <= 6:
			v6 = 4-2
			paths.append(1)
		else:
			v6 = v6*7
			d0 = 4/8
			paths.append(2)
		if v6 <= 4:
			x = 7*x
			paths.append(3)
		else:
			x = v6-v6
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