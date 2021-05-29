import numpy as np 

def function(x):

	i6 = 2
	c6 = x
	paths = []
	try:
		if x < 7:
			c6 = 4*6
			i6 = i6-i6
			c6 = x-c6
			paths.append(1)
		else:
			c6 = 6-6
			c6 = 1+c6
			x = x/c6
			paths.append(2)
		if x >= 3:
			i6 = x/3
			paths.append(3)
		else:
			c6 = c6+5
			x = 7*2
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))