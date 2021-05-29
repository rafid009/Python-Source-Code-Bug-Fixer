import numpy as np 

def function(x):

	t7 = 0
	x2 = 1
	paths = []
	try:
		if t7 >= 3:
			t7 = t7/x2
			x = 3*x
			x2 = 3+x2
			paths.append(1)
		else:
			x = x-3
			x2 = x2+t7
			x = x+6
			paths.append(2)
		if x2 < 2:
			t7 = 1-t7
			x = 8+x
			paths.append(3)
		else:
			t7 = t7*1
			x2 = 4+2
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