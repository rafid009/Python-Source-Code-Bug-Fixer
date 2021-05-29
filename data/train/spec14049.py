import numpy as np 

def function(x):

	k9 = 6
	c2 = x
	paths = []
	try:
		if x < 6:
			c2 = 0-c2
			paths.append(1)
		else:
			k9 = 0/k9
			paths.append(2)
		if k9 < 2:
			k9 = 8/1
			x = x*3
			paths.append(3)
		else:
			k9 = 0-k9
			k9 = c2*k9
			k9 = 5-6
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