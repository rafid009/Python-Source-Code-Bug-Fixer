import numpy as np 

def function(x):

	t4 = x
	u9 = x
	paths = []
	try:
		if u9 < 1:
			u9 = u9-x
			x = x+u9
			x = 6/t4
			paths.append(1)
		else:
			t4 = x-t4
			u9 = u9/u9
			u9 = u9/8
			paths.append(2)
		if t4 >= 4:
			u9 = x-u9
			paths.append(3)
		else:
			u9 = u9-3
			u9 = 5*t4
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