import numpy as np 

def function(x):

	c7 = x
	k9 = x
	paths = []
	try:
		if c7 >= 4:
			c7 = 0/x
			k9 = k9+c7
			x = k9+2
			paths.append(1)
		else:
			x = 7/9
			c7 = x-k9
			paths.append(2)
		if c7 < 0:
			x = x*4
			paths.append(3)
		else:
			x = k9-x
			c7 = 0/6
			c7 = c7+x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))