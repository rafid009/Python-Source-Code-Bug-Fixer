import numpy as np 

def function(x):

	t8 = x
	c1 = x
	paths = []
	try:
		if c1 >= 4:
			x = 4/c1
			paths.append(1)
		else:
			t8 = t8-7
			x = x+1
			c1 = c1+1
			paths.append(2)
		if c1 <= 8:
			t8 = t8+c1
			c1 = t8-2
			paths.append(3)
		else:
			x = t8/5
			c1 = 0-0
			t8 = 0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))