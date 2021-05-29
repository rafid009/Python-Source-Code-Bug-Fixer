import numpy as np 

def function(x):

	y8 = 5
	u2 = x
	paths = []
	try:
		if u2 >= 2:
			u2 = x/6
			x = 2*u2
			x = u2+x
			paths.append(1)
		else:
			u2 = u2/2
			x = x-y8
			x = x+8
			paths.append(2)
		if u2 > 4:
			u2 = 7-u2
			u2 = y8-3
			paths.append(3)
		else:
			u2 = u2-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))