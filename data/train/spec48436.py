import numpy as np 

def function(x):

	c1 = 7
	t3 = x
	paths = []
	try:
		if x >= 3:
			c1 = c1/c1
			t3 = t3/9
			x = t3*c1
			paths.append(1)
		else:
			c1 = 6*1
			x = 0/x
			paths.append(2)
		if x < 1:
			c1 = c1+0
			c1 = c1+2
			paths.append(3)
		else:
			x = 2/5
			c1 = c1-c1
			t3 = t3*2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))