import numpy as np 

def function(x):

	c3 = 3
	l3 = 3
	paths = []
	try:
		if c3 < 3:
			c3 = c3*1
			x = x-4
			x = 2/x
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if c3 < 6:
			c3 = 0-c3
			x = 3*7
			x = x/8
			paths.append(3)
		else:
			l3 = 5*9
			l3 = l3*5
			l3 = 9+l3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		l3 = c3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))