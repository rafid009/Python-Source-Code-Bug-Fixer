import numpy as np 

def function(x):

	t7 = 7
	c6 = x
	paths = []
	try:
		if c6 <= 3:
			x = x-9
			t7 = 6*t7
			t7 = 9/3
			paths.append(1)
		else:
			x = c6*6
			paths.append(2)
		if t7 > 9:
			x = x+5
			t7 = t7+5
			x = 2*x
			paths.append(3)
		else:
			c6 = t7-c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))