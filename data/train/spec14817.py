import numpy as np 

def function(x):

	a8 = x
	k5 = 5
	paths = []
	try:
		if k5 <= 3:
			x = 2*a8
			paths.append(1)
		else:
			k5 = a8*k5
			paths.append(2)
		if x >= 9:
			a8 = 1+a8
			paths.append(3)
		else:
			k5 = k5*2
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