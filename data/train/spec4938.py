import numpy as np 

def function(x):

	l6 = 1
	c9 = x
	x = 2
	paths = []
	try:
		if l6 < 9:
			l6 = 3-9
			l6 = l6+0
			paths.append(1)
		else:
			l6 = 5+0
			l6 = 2+l6
			c9 = c9-2
			paths.append(2)
		if c9 < 3:
			l6 = l6*5
			l6 = c9/7
			paths.append(3)
		else:
			x = x+l6
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