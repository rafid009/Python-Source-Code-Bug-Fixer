import numpy as np 

def function(x):

	t7 = x
	l7 = 1
	paths = []
	try:
		if x >= 0:
			t7 = l7+x
			x = l7-7
			paths.append(1)
		else:
			x = 4+4
			t7 = t7/t7
			x = x/9
			paths.append(2)
		if l7 < 0:
			t7 = 6*8
			paths.append(3)
		else:
			t7 = 9+t7
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