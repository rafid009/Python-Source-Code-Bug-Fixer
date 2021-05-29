import numpy as np 

def function(x):

	c2 = 4
	r7 = 5
	paths = []
	try:
		if r7 <= 7:
			r7 = r7*6
			c2 = 8+4
			c2 = 8-x
			paths.append(1)
		else:
			x = x+1
			c2 = c2*1
			paths.append(2)
		if x < 0:
			x = x*7
			paths.append(3)
		else:
			x = 3+0
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))