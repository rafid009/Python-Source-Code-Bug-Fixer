import numpy as np 

def function(x):

	c3 = 5
	k9 = x
	paths = []
	try:
		if c3 >= 1:
			x = 6/x
			x = 9-k9
			paths.append(1)
		else:
			c3 = k9-9
			x = c3+1
			paths.append(2)
		if k9 > 2:
			k9 = 4-0
			paths.append(3)
		else:
			k9 = 5*k9
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