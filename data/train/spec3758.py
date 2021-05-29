import numpy as np 

def function(x):

	c2 = 1
	a2 = x
	paths = []
	try:
		if c2 <= 1:
			x = x/6
			c2 = c2/9
			c2 = c2*a2
			paths.append(1)
		else:
			x = 2-c2
			x = x-5
			x = 7*a2
			paths.append(2)
		if c2 > 5:
			c2 = c2+1
			a2 = a2/a2
			paths.append(3)
		else:
			c2 = c2+1
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))