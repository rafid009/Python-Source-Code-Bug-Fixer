import numpy as np 

def function(x):

	a0 = 8
	v6 = 8
	paths = []
	try:
		if v6 >= 0:
			a0 = 0-3
			x = 9+x
			paths.append(1)
		else:
			x = a0/4
			a0 = a0-6
			x = 8+v6
			paths.append(2)
		if x > 1:
			x = a0+x
			v6 = v6/x
			paths.append(3)
		else:
			x = x-2
			v6 = v6+3
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))