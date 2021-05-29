import numpy as np 

def function(x):

	a8 = x
	t0 = 8
	paths = []
	try:
		if a8 >= 2:
			x = x/x
			a8 = a8*a8
			paths.append(1)
		else:
			a8 = a8-1
			a8 = a8*3
			t0 = 6*9
			paths.append(2)
		if x > 1:
			a8 = a8+0
			paths.append(3)
		else:
			a8 = a8*1
			a8 = 5/a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))