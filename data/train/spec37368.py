import numpy as np 

def function(x):

	c6 = 7
	t3 = x
	paths = []
	try:
		if t3 >= 0:
			c6 = 5+t3
			paths.append(1)
		else:
			t3 = 1*t3
			c6 = 2-x
			x = 7+0
			paths.append(2)
		if x <= 6:
			x = x*4
			paths.append(3)
		else:
			x = x-x
			c6 = c6-8
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