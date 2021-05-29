import numpy as np 

def function(x):

	c3 = 4
	u1 = 2
	paths = []
	try:
		if c3 < 0:
			x = x/c3
			paths.append(1)
		else:
			u1 = 5*7
			u1 = c3-u1
			paths.append(2)
		if x > 2:
			x = u1+x
			u1 = u1*1
			x = x-7
			paths.append(3)
		else:
			x = 2*1
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