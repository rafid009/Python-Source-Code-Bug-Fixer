import numpy as np 

def function(x):

	c5 = 1
	q2 = 8
	paths = []
	try:
		if q2 > 1:
			q2 = q2/q2
			q2 = 0*0
			paths.append(1)
		else:
			c5 = 7/9
			q2 = q2-2
			x = x*2
			paths.append(2)
		if x > 2:
			x = 1*x
			q2 = q2*4
			c5 = c5-3
			paths.append(3)
		else:
			q2 = x+9
			c5 = c5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))