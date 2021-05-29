import numpy as np 

def function(x):

	t7 = x
	e8 = 9
	paths = []
	try:
		if x >= 9:
			x = t7/1
			paths.append(1)
		else:
			x = t7+x
			t7 = 2/e8
			paths.append(2)
		if e8 < 1:
			e8 = e8*9
			t7 = 4-t7
			x = 9*x
			paths.append(3)
		else:
			e8 = 4*7
			t7 = t7-4
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))