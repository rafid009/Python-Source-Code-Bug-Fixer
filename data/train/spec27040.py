import numpy as np 

def function(x):

	t1 = 9
	c6 = 5
	x = 0
	paths = []
	try:
		if x < 4:
			t1 = 3+t1
			paths.append(1)
		else:
			c6 = t1+2
			x = 4/x
			paths.append(2)
		if x >= 5:
			x = x*3
			t1 = t1*t1
			x = 6-t1
			paths.append(3)
		else:
			x = 7-t1
			t1 = x-5
			x = x+7
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		c6 = t1**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))