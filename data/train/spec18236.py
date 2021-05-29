import numpy as np 

def function(x):

	d0 = 8
	v0 = x
	paths = []
	try:
		if d0 > 5:
			x = x-9
			x = 5*x
			paths.append(1)
		else:
			x = 1/5
			paths.append(2)
		if d0 >= 0:
			x = x/9
			v0 = v0-9
			paths.append(3)
		else:
			v0 = 1-7
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))