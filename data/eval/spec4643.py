import numpy as np 

def function(x):

	k3 = 2
	c2 = x
	paths = []
	try:
		if k3 >= 1:
			x = 3+x
			paths.append(1)
		else:
			c2 = k3*c2
			paths.append(2)
		if c2 <= 0:
			c2 = 0+c2
			x = k3-7
			k3 = 3*k3
			paths.append(3)
		else:
			x = x*8
			c2 = 5+c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		k3 = c2**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))