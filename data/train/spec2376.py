import numpy as np 

def function(x):

	t7 = 2
	x6 = x
	paths = []
	try:
		if x6 < 0:
			t7 = t7*x
			paths.append(1)
		else:
			x6 = 0-x6
			x = t7/8
			t7 = t7-3
			paths.append(2)
		if x <= 6:
			t7 = t7*7
			x = 7*x
			t7 = t7+4
			paths.append(3)
		else:
			t7 = 3/t7
			x = t7+8
			x6 = x/4
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))