import numpy as np 

def function(x):

	u6 = x
	t8 = x
	paths = []
	try:
		if t8 >= 9:
			x = 5-x
			t8 = 2+6
			paths.append(1)
		else:
			t8 = 7/t8
			u6 = 6-u6
			paths.append(2)
		if x > 1:
			u6 = u6/t8
			x = x/3
			paths.append(3)
		else:
			u6 = 4-u6
			x = x+x
			x = 8+x
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