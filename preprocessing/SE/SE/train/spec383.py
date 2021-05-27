import numpy as np 

def function(x):

	a0 = 0
	c1 = x
	paths = []
	try:
		if c1 <= 8:
			x = c1+x
			paths.append(1)
		else:
			c1 = a0/1
			a0 = 4-a0
			paths.append(2)
		if x <= 0:
			a0 = a0+c1
			c1 = 4*c1
			paths.append(3)
		else:
			a0 = c1+a0
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		a0 = c1**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))