import numpy as np 

def function(x):

	l6 = 4
	c8 = x
	paths = []
	try:
		if c8 > 2:
			x = c8/x
			paths.append(1)
		else:
			l6 = 8+l6
			paths.append(2)
		if x > 1:
			x = l6/5
			paths.append(3)
		else:
			x = 0+x
			x = x+3
			x = 2+1
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		l6 = c8**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))