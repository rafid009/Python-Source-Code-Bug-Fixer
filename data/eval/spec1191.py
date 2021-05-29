import numpy as np 

def function(x):

	t4 = 7
	c5 = 6
	paths = []
	try:
		if c5 > 8:
			c5 = 3/c5
			paths.append(1)
		else:
			c5 = c5-8
			c5 = 4*c5
			t4 = t4*8
			paths.append(2)
		if t4 < 6:
			x = 0*9
			t4 = t4*0
			t4 = t4*9
			paths.append(3)
		else:
			x = 1+x
			t4 = x*t4
			c5 = c5-9
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))