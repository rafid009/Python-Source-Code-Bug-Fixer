import numpy as np 

def function(x):

	i6 = 1
	c8 = 8
	paths = []
	try:
		if i6 <= 2:
			c8 = 2-8
			i6 = 7+i6
			paths.append(1)
		else:
			i6 = 1+i6
			x = x/c8
			paths.append(2)
		if i6 < 7:
			i6 = i6/i6
			i6 = 5/i6
			x = x+c8
			paths.append(3)
		else:
			c8 = 1/c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		i6 = c8**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))