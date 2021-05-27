import numpy as np 

def function(x):

	c3 = 6
	u2 = x
	paths = []
	try:
		if x <= 6:
			x = x*2
			x = 5-x
			paths.append(1)
		else:
			x = u2-u2
			paths.append(2)
		if u2 >= 7:
			x = 9*x
			u2 = x*7
			paths.append(3)
		else:
			c3 = 6+c3
			c3 = u2*c3
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))