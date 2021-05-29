import numpy as np 

def function(x):

	x9 = 5
	t4 = 1
	paths = []
	try:
		if x9 <= 0:
			x = x+x
			paths.append(1)
		else:
			t4 = t4-4
			t4 = 6*t4
			paths.append(2)
		if x9 >= 8:
			x9 = x9-x
			x9 = t4-x9
			paths.append(3)
		else:
			x9 = x9*x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x9 = t4**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))