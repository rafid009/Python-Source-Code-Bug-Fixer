import numpy as np 

def function(x):

	k9 = x
	c2 = 9
	paths = []
	try:
		if k9 < 7:
			x = 5+c2
			k9 = k9*x
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if c2 >= 1:
			x = c2-x
			paths.append(3)
		else:
			c2 = c2/9
			x = k9/x
			k9 = 0*k9
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