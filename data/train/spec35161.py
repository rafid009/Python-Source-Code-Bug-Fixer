import numpy as np 

def function(x):

	c1 = 5
	i6 = x
	paths = []
	try:
		if x < 1:
			c1 = 6*c1
			x = x-c1
			x = x*5
			paths.append(1)
		else:
			c1 = c1-4
			x = i6/x
			x = x/1
			paths.append(2)
		if x >= 6:
			c1 = c1*0
			x = x-6
			paths.append(3)
		else:
			c1 = c1+8
			i6 = 6-i6
			i6 = i6/4
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))