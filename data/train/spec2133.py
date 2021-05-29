import numpy as np 

def function(x):

	c9 = x
	k3 = 1
	paths = []
	try:
		if x > 5:
			c9 = c9*c9
			x = x-4
			k3 = 5+c9
			paths.append(1)
		else:
			k3 = 4/k3
			paths.append(2)
		if x > 7:
			c9 = x-c9
			c9 = 0/4
			paths.append(3)
		else:
			x = x+7
			c9 = c9-5
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		k3 = c9**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))