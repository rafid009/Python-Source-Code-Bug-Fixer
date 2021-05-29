import numpy as np 

def function(x):

	l4 = 2
	k5 = x
	paths = []
	try:
		if k5 > 3:
			l4 = l4*3
			k5 = 6/8
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if l4 > 5:
			x = 0+l4
			k5 = 9-k5
			l4 = 2*k5
			paths.append(3)
		else:
			l4 = l4*x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))