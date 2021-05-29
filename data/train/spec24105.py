import numpy as np 

def function(x):

	b3 = x
	c7 = x
	paths = []
	try:
		if b3 > 7:
			x = 7/c7
			x = b3*8
			x = x+9
			paths.append(1)
		else:
			b3 = b3-5
			b3 = 8+c7
			paths.append(2)
		if x <= 1:
			x = x+7
			paths.append(3)
		else:
			c7 = c7+5
			c7 = x+c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))