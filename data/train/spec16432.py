import numpy as np 

def function(x):

	t5 = x
	c6 = 8
	paths = []
	try:
		if c6 < 8:
			c6 = c6-7
			x = 8-7
			x = x+t5
			paths.append(1)
		else:
			t5 = c6*t5
			x = 9*c6
			paths.append(2)
		if t5 >= 5:
			x = t5+c6
			paths.append(3)
		else:
			c6 = 2-1
			c6 = 4/x
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))