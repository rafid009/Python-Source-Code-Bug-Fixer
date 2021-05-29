import numpy as np 

def function(x):

	t9 = x
	i6 = x
	x = x
	paths = []
	try:
		if i6 < 7:
			i6 = 3+t9
			t9 = 7-0
			paths.append(1)
		else:
			i6 = 7/i6
			paths.append(2)
		if t9 < 1:
			t9 = 7*5
			t9 = i6-t9
			paths.append(3)
		else:
			i6 = i6*6
			t9 = 6+t9
			x = x-8
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