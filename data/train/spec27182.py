import numpy as np 

def function(x):

	c5 = x
	t6 = x
	paths = []
	try:
		if c5 >= 8:
			t6 = 1-t6
			t6 = t6*4
			paths.append(1)
		else:
			c5 = c5-3
			x = 8+x
			c5 = c5-4
			paths.append(2)
		if c5 > 5:
			c5 = t6+2
			paths.append(3)
		else:
			c5 = c5+t6
			c5 = c5-6
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		t6 = c5**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))