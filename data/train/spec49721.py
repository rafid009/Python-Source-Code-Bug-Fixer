import numpy as np 

def function(x):

	t8 = 1
	c6 = x
	paths = []
	try:
		if x > 8:
			t8 = c6-t8
			x = x/x
			paths.append(1)
		else:
			t8 = 5+c6
			paths.append(2)
		if c6 > 7:
			t8 = c6-2
			paths.append(3)
		else:
			x = 4-c6
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))