import numpy as np 

def function(x):

	a4 = 7
	t9 = 3
	paths = []
	try:
		if t9 < 2:
			x = a4+x
			x = 0+x
			paths.append(1)
		else:
			x = 2/x
			x = x-0
			paths.append(2)
		if a4 <= 4:
			t9 = 4*t9
			t9 = 4/5
			x = x/t9
			paths.append(3)
		else:
			a4 = 8/9
			a4 = 9+a4
			a4 = 8-a4
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