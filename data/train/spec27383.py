import numpy as np 

def function(x):

	r1 = x
	c3 = x
	paths = []
	try:
		if x > 6:
			r1 = r1+1
			c3 = 8*9
			paths.append(1)
		else:
			r1 = c3*6
			x = x*x
			paths.append(2)
		if x > 2:
			x = x-c3
			r1 = 2+8
			c3 = c3-1
			paths.append(3)
		else:
			x = x*c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		r1 = c3**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))