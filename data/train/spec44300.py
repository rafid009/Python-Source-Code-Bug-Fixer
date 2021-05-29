import numpy as np 

def function(x):

	u2 = 4
	l7 = 4
	paths = []
	try:
		if u2 < 8:
			x = 4-3
			u2 = 0-u2
			paths.append(1)
		else:
			u2 = u2+8
			x = x+8
			x = x/1
			paths.append(2)
		if u2 >= 6:
			l7 = l7+l7
			paths.append(3)
		else:
			x = 9-5
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))