import numpy as np 

def function(x):

	c5 = x
	l6 = x
	paths = []
	try:
		if l6 >= 8:
			x = 0/3
			x = 7*0
			x = 8+x
			paths.append(1)
		else:
			l6 = 6+x
			paths.append(2)
		if l6 <= 3:
			c5 = 6+4
			x = 6+c5
			paths.append(3)
		else:
			x = x/l6
			x = x+3
			x = c5-c5
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		c5 = l6**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))