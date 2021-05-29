import numpy as np 

def function(x):

	c7 = x
	j3 = x
	paths = []
	try:
		if j3 >= 6:
			x = j3-x
			j3 = 4+x
			paths.append(1)
		else:
			j3 = j3*c7
			c7 = c7*c7
			paths.append(2)
		if j3 <= 6:
			j3 = 2*4
			paths.append(3)
		else:
			c7 = x*2
			c7 = 1+5
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