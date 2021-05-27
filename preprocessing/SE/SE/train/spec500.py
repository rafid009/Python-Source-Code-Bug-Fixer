import numpy as np 

def function(x):

	r7 = 4
	c2 = 8
	paths = []
	try:
		if c2 < 7:
			c2 = x-c2
			r7 = r7+3
			x = r7*c2
			paths.append(1)
		else:
			r7 = r7-c2
			paths.append(2)
		if c2 >= 6:
			c2 = 8*c2
			r7 = x+1
			paths.append(3)
		else:
			x = x-c2
			c2 = r7/7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))