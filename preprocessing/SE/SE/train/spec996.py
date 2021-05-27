import numpy as np 

def function(x):

	c2 = 3
	i6 = 8
	paths = []
	try:
		if i6 >= 1:
			x = 0-x
			paths.append(1)
		else:
			i6 = 7*i6
			paths.append(2)
		if x > 4:
			i6 = c2-3
			i6 = i6*0
			paths.append(3)
		else:
			i6 = i6*c2
			i6 = 0-i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		c2 = i6**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))