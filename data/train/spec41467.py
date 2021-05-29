import numpy as np 

def function(x):

	l3 = x
	c5 = 0
	paths = []
	try:
		if l3 <= 2:
			x = x-7
			paths.append(1)
		else:
			x = 9/x
			c5 = c5+3
			paths.append(2)
		if x >= 9:
			c5 = x/9
			c5 = c5*c5
			x = 6-x
			paths.append(3)
		else:
			c5 = c5-l3
			c5 = 7+c5
			l3 = l3*7
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))