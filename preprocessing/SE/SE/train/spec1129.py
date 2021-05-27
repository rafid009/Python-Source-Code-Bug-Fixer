import numpy as np 

def function(x):

	c1 = x
	l2 = 6
	paths = []
	try:
		if l2 > 9:
			l2 = l2+x
			c1 = 8-6
			paths.append(1)
		else:
			c1 = 8*c1
			c1 = c1*4
			l2 = 2-5
			paths.append(2)
		if x < 8:
			l2 = l2+2
			x = x-l2
			c1 = c1-6
			paths.append(3)
		else:
			c1 = c1+7
			x = x+c1
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))