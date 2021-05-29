import numpy as np 

def function(x):

	v7 = x
	c0 = 5
	paths = []
	try:
		if x >= 7:
			x = x*2
			v7 = 2*4
			paths.append(1)
		else:
			c0 = 9/9
			x = x+4
			x = 6+4
			paths.append(2)
		if v7 > 8:
			v7 = 2-9
			x = v7/x
			paths.append(3)
		else:
			c0 = 5-4
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))