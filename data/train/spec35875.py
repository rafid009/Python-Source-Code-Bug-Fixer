import numpy as np 

def function(x):

	a6 = x
	t7 = 6
	paths = []
	try:
		if t7 <= 2:
			a6 = a6*a6
			paths.append(1)
		else:
			a6 = t7/a6
			paths.append(2)
		if x > 4:
			x = a6*9
			paths.append(3)
		else:
			a6 = 4+a6
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