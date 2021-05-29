import numpy as np 

def function(x):

	q8 = x
	c1 = x
	paths = []
	try:
		if c1 <= 7:
			x = 2+x
			q8 = q8*x
			paths.append(1)
		else:
			q8 = q8+7
			x = x+8
			paths.append(2)
		if x < 2:
			x = x-1
			c1 = c1-6
			x = x*q8
			paths.append(3)
		else:
			x = 1-x
			q8 = 2*3
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))