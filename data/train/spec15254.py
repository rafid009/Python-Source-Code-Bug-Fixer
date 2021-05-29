import numpy as np 

def function(x):

	f4 = x
	t6 = 3
	paths = []
	try:
		if x < 9:
			x = 3+x
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if f4 < 0:
			t6 = t6/x
			paths.append(3)
		else:
			t6 = t6-0
			x = x-x
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))