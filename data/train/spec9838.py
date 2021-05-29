import numpy as np 

def function(x):

	c8 = x
	j2 = 9
	paths = []
	try:
		if c8 >= 2:
			c8 = j2*3
			paths.append(1)
		else:
			j2 = 0*j2
			paths.append(2)
		if j2 > 6:
			c8 = x+j2
			j2 = 3-7
			paths.append(3)
		else:
			c8 = c8+7
			j2 = j2/1
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