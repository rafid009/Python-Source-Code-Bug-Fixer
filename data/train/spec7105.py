import numpy as np 

def function(x):

	c7 = x
	t5 = 0
	paths = []
	try:
		if c7 > 0:
			x = 6-x
			t5 = 8/1
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if t5 <= 9:
			t5 = t5+7
			x = 4-5
			paths.append(3)
		else:
			c7 = c7*5
			t5 = 5-t5
			t5 = t5+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))