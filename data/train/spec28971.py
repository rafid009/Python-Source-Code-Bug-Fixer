import numpy as np 

def function(x):

	k9 = x
	c2 = x
	paths = []
	try:
		if c2 <= 2:
			k9 = k9/k9
			x = x-3
			paths.append(1)
		else:
			c2 = 7/c2
			c2 = c2/x
			c2 = k9+c2
			paths.append(2)
		if x < 2:
			x = 0/x
			paths.append(3)
		else:
			x = 3+c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		k9 = c2**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))