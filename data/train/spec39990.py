import numpy as np 

def function(x):

	v3 = 4
	c8 = 1
	paths = []
	try:
		if x < 9:
			x = 0+x
			c8 = c8*8
			x = 1-x
			paths.append(1)
		else:
			c8 = c8+c8
			paths.append(2)
		if x > 7:
			v3 = v3/9
			v3 = v3-x
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))