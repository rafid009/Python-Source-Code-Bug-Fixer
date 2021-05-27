import numpy as np 

def function(x):

	c2 = x
	k3 = x
	paths = []
	try:
		if k3 >= 1:
			c2 = 3-8
			k3 = 5/c2
			paths.append(1)
		else:
			c2 = 7+c2
			x = 9*x
			paths.append(2)
		if c2 <= 6:
			x = x/3
			k3 = 0*x
			x = 1+k3
			paths.append(3)
		else:
			c2 = c2-4
			x = x+9
			c2 = c2/c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))