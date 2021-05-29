import numpy as np 

def function(x):

	r2 = x
	c7 = 4
	paths = []
	try:
		if r2 >= 1:
			c7 = c7*1
			r2 = c7+r2
			paths.append(1)
		else:
			x = 2-3
			x = 7*r2
			paths.append(2)
		if c7 <= 3:
			r2 = 5+x
			r2 = r2-c7
			paths.append(3)
		else:
			c7 = r2*c7
			c7 = 2/r2
			r2 = r2+1
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		r2 = c7**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))