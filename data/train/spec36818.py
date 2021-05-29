import numpy as np 

def function(x):

	t7 = x
	x4 = 3
	paths = []
	try:
		if x4 >= 4:
			x = 9+x
			x = x*x4
			paths.append(1)
		else:
			x4 = 7+x4
			paths.append(2)
		if x4 > 8:
			x4 = t7*x4
			paths.append(3)
		else:
			t7 = t7*t7
			x4 = 6-x4
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))