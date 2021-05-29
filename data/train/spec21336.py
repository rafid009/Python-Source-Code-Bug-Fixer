import numpy as np 

def function(x):

	c2 = x
	t0 = x
	paths = []
	try:
		if x <= 1:
			t0 = x/3
			x = x/3
			paths.append(1)
		else:
			t0 = 8+t0
			t0 = t0+t0
			c2 = 1-x
			paths.append(2)
		if t0 <= 4:
			x = 8+x
			x = 9-x
			c2 = c2+8
			paths.append(3)
		else:
			x = c2+0
			t0 = t0/t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))