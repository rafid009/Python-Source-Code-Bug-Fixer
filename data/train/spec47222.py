import numpy as np 

def function(x):

	l1 = x
	c6 = 8
	paths = []
	try:
		if l1 < 0:
			x = 2+x
			x = 3-x
			c6 = l1-8
			paths.append(1)
		else:
			l1 = 1/9
			x = l1-l1
			c6 = 0-c6
			paths.append(2)
		if c6 <= 5:
			l1 = l1-5
			paths.append(3)
		else:
			c6 = c6*2
			l1 = x*x
			l1 = l1/9
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))