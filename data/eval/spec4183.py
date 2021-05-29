import numpy as np 

def function(x):

	c8 = 0
	k6 = x
	paths = []
	try:
		if x <= 8:
			x = 1+x
			c8 = c8*x
			paths.append(1)
		else:
			c8 = c8/6
			paths.append(2)
		if k6 >= 5:
			c8 = c8+6
			c8 = c8+3
			paths.append(3)
		else:
			x = x*8
			c8 = c8*5
			k6 = k6*1
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))