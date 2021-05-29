import numpy as np 

def function(x):

	j0 = 2
	u2 = 5
	paths = []
	try:
		if u2 <= 2:
			x = u2/x
			u2 = 0/5
			paths.append(1)
		else:
			j0 = u2/7
			paths.append(2)
		if j0 >= 2:
			u2 = 7-7
			paths.append(3)
		else:
			u2 = 9*3
			u2 = u2/4
			j0 = j0*2
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