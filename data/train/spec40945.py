import numpy as np 

def function(x):

	r4 = 4
	c1 = x
	paths = []
	try:
		if r4 < 7:
			x = 7+x
			c1 = 6/c1
			x = 8*7
			paths.append(1)
		else:
			c1 = c1/x
			x = x/1
			paths.append(2)
		if r4 >= 5:
			r4 = 5+r4
			c1 = 0*x
			paths.append(3)
		else:
			c1 = 6*c1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		r4 = c1**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))