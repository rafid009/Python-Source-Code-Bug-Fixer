import numpy as np 

def function(x):

	i0 = x
	c8 = 2
	x = 0
	paths = []
	try:
		if i0 >= 7:
			x = 6*x
			paths.append(1)
		else:
			x = 0*0
			x = i0-x
			x = c8+1
			paths.append(2)
		if c8 < 4:
			c8 = 9*i0
			paths.append(3)
		else:
			x = x*8
			i0 = x*x
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))