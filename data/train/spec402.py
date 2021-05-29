import numpy as np 

def function(x):

	i0 = 7
	u0 = 4
	paths = []
	try:
		if u0 >= 8:
			x = 2-x
			x = x+1
			paths.append(1)
		else:
			u0 = 5-3
			u0 = u0/8
			paths.append(2)
		if x <= 9:
			x = 4+x
			paths.append(3)
		else:
			u0 = 3-u0
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))