import numpy as np 

def function(x):

	c7 = x
	q0 = x
	paths = []
	try:
		if c7 >= 3:
			c7 = c7*3
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if q0 <= 9:
			q0 = q0/3
			x = x+x
			paths.append(3)
		else:
			c7 = q0-7
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))