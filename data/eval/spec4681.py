import numpy as np 

def function(x):

	k9 = 2
	c8 = x
	paths = []
	try:
		if x >= 4:
			x = c8*6
			k9 = k9+4
			paths.append(1)
		else:
			c8 = c8/1
			c8 = c8-x
			c8 = k9-1
			paths.append(2)
		if k9 > 8:
			x = 6-c8
			c8 = 8+0
			paths.append(3)
		else:
			k9 = x+k9
			x = k9+x
			x = x*8
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