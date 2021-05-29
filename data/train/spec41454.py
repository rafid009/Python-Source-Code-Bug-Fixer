import numpy as np 

def function(x):

	t6 = x
	c3 = 5
	paths = []
	try:
		if c3 > 3:
			x = t6/x
			x = 4*5
			x = t6+7
			paths.append(1)
		else:
			t6 = 8+t6
			paths.append(2)
		if c3 < 9:
			t6 = t6+3
			c3 = c3-5
			t6 = c3+t6
			paths.append(3)
		else:
			t6 = 7/t6
			c3 = 5+t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))