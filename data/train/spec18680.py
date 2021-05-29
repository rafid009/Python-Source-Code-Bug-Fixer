import numpy as np 

def function(x):

	b2 = x
	k4 = 2
	paths = []
	try:
		if k4 < 6:
			b2 = b2/1
			b2 = b2*9
			paths.append(1)
		else:
			b2 = b2*4
			x = 0/k4
			k4 = k4+7
			paths.append(2)
		if k4 >= 0:
			x = 0*x
			paths.append(3)
		else:
			b2 = 7-k4
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))