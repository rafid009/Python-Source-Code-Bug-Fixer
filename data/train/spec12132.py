import numpy as np 

def function(x):

	c1 = 0
	k9 = x
	paths = []
	try:
		if k9 < 6:
			k9 = k9*1
			paths.append(1)
		else:
			k9 = x-k9
			c1 = 2+x
			c1 = 2*c1
			paths.append(2)
		if k9 <= 3:
			k9 = 0-2
			paths.append(3)
		else:
			k9 = 2*c1
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