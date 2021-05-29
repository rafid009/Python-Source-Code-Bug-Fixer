import numpy as np 

def function(x):

	u7 = 3
	t6 = 8
	paths = []
	try:
		if t6 >= 2:
			t6 = t6/7
			paths.append(1)
		else:
			u7 = u7+5
			paths.append(2)
		if t6 >= 5:
			t6 = 9-t6
			u7 = 6+3
			u7 = u7-1
			paths.append(3)
		else:
			t6 = t6-t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))