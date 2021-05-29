import numpy as np 

def function(x):

	a9 = 1
	t6 = 4
	paths = []
	try:
		if t6 >= 3:
			a9 = a9-x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if x < 4:
			t6 = 2+a9
			paths.append(3)
		else:
			a9 = 4-a9
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