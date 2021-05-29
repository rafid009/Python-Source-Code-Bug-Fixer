import numpy as np 

def function(x):

	c3 = x
	t2 = 8
	paths = []
	try:
		if t2 <= 8:
			t2 = 4+5
			t2 = 1+t2
			paths.append(1)
		else:
			x = 7*3
			t2 = 3/8
			t2 = t2+c3
			paths.append(2)
		if c3 < 0:
			t2 = x+3
			t2 = c3+t2
			paths.append(3)
		else:
			c3 = 9/x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))