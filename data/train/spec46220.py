import numpy as np 

def function(x):

	t8 = x
	a3 = x
	paths = []
	try:
		if t8 <= 1:
			t8 = t8*6
			a3 = a3+x
			x = a3-x
			paths.append(1)
		else:
			x = t8-x
			paths.append(2)
		if t8 < 0:
			a3 = x-8
			paths.append(3)
		else:
			t8 = x/t8
			a3 = t8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))