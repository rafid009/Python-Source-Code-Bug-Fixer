import numpy as np 

def function(x):

	c3 = x
	t2 = x
	paths = []
	try:
		if c3 < 5:
			x = 3*x
			t2 = 4*x
			paths.append(1)
		else:
			t2 = 4+x
			t2 = t2+3
			t2 = 2/t2
			paths.append(2)
		if t2 > 9:
			t2 = t2-c3
			x = 7-6
			paths.append(3)
		else:
			t2 = t2+4
			t2 = 3+c3
			c3 = c3-6
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		c3 = t2**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))