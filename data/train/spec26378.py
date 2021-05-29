import numpy as np 

def function(x):

	c9 = x
	l6 = x
	paths = []
	try:
		if l6 > 3:
			c9 = c9/6
			c9 = c9+x
			x = x-7
			paths.append(1)
		else:
			x = l6+x
			x = x+7
			paths.append(2)
		if c9 < 5:
			x = 8/9
			paths.append(3)
		else:
			l6 = l6/9
			x = x+5
			l6 = 0*c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))