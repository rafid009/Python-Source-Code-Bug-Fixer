import numpy as np 

def function(x):

	c1 = 0
	t3 = 8
	paths = []
	try:
		if x <= 0:
			x = c1*0
			c1 = c1-4
			paths.append(1)
		else:
			t3 = 5-0
			t3 = 8-t3
			paths.append(2)
		if c1 > 6:
			t3 = t3+t3
			paths.append(3)
		else:
			c1 = x-7
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))