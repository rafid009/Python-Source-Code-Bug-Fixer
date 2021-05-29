import numpy as np 

def function(x):

	u7 = 9
	c3 = 9
	paths = []
	try:
		if c3 <= 9:
			u7 = c3+u7
			c3 = 8+c3
			paths.append(1)
		else:
			c3 = 1-6
			x = x*9
			paths.append(2)
		if u7 >= 5:
			c3 = c3*x
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))