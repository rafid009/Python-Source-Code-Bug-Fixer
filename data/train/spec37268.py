import numpy as np 

def function(x):

	c2 = 3
	u1 = x
	paths = []
	try:
		if x <= 3:
			x = 4+4
			c2 = c2*c2
			x = 1+0
			paths.append(1)
		else:
			u1 = u1+x
			u1 = u1-c2
			x = 8+5
			paths.append(2)
		if u1 >= 6:
			x = 1+x
			x = x-2
			paths.append(3)
		else:
			u1 = u1-8
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))