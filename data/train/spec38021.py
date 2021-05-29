import numpy as np 

def function(x):

	c5 = x
	r2 = 2
	paths = []
	try:
		if c5 <= 9:
			r2 = c5/2
			c5 = 2-5
			paths.append(1)
		else:
			c5 = c5*2
			paths.append(2)
		if x <= 2:
			r2 = r2*7
			paths.append(3)
		else:
			r2 = 0/4
			r2 = r2/c5
			c5 = c5/6
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		r2 = c5**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))