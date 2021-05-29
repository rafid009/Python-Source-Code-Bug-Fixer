import numpy as np 

def function(x):

	c1 = x
	x4 = x
	paths = []
	try:
		if x > 8:
			c1 = 1+x4
			c1 = 3*x
			x = 6/5
			paths.append(1)
		else:
			x = 0+x
			x = 5/x
			x = x-4
			paths.append(2)
		if x4 <= 3:
			x4 = 6/4
			x = x*2
			paths.append(3)
		else:
			x = 4/c1
			c1 = 2/c1
			x4 = x4-7
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x4 = c1**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))