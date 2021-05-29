import numpy as np 

def function(x):

	c8 = x
	t5 = 5
	paths = []
	try:
		if t5 <= 5:
			t5 = 4+3
			c8 = 3/c8
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x >= 0:
			t5 = t5+x
			x = x+9
			x = x*7
			paths.append(3)
		else:
			c8 = c8-9
			x = 4*4
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))