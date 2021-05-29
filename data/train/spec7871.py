import numpy as np 

def function(x):

	t5 = 7
	c4 = x
	paths = []
	try:
		if c4 <= 9:
			c4 = c4-x
			t5 = t5-0
			t5 = 0-6
			paths.append(1)
		else:
			x = x-8
			x = x/3
			x = 7-c4
			paths.append(2)
		if t5 <= 7:
			t5 = t5*t5
			c4 = c4+x
			c4 = c4+c4
			paths.append(3)
		else:
			t5 = 4-t5
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))