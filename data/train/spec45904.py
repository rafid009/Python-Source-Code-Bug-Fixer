import numpy as np 

def function(x):

	i6 = 2
	t8 = 8
	paths = []
	try:
		if t8 < 6:
			x = i6-t8
			t8 = t8-7
			i6 = 8*t8
			paths.append(1)
		else:
			i6 = i6/x
			i6 = i6/9
			paths.append(2)
		if t8 < 6:
			t8 = t8/t8
			x = x-0
			paths.append(3)
		else:
			x = i6-x
			t8 = 2/6
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