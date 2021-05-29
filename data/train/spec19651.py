import numpy as np 

def function(x):

	c2 = 4
	e6 = x
	paths = []
	try:
		if x > 7:
			x = x/2
			c2 = 5+9
			c2 = c2-e6
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if e6 < 5:
			c2 = 6*c2
			c2 = c2-9
			paths.append(3)
		else:
			e6 = e6+e6
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