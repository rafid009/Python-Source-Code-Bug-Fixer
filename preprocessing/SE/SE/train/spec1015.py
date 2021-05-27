import numpy as np 

def function(x):

	c1 = x
	r5 = 0
	paths = []
	try:
		if c1 >= 8:
			x = x+2
			r5 = 7+x
			c1 = 2+4
			paths.append(1)
		else:
			x = 5*x
			x = c1-x
			x = 9+0
			paths.append(2)
		if r5 >= 3:
			x = c1*9
			r5 = 6+4
			c1 = 2/c1
			paths.append(3)
		else:
			x = 1*r5
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		r5 = c1**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))