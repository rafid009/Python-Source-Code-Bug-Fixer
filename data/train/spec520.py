import numpy as np 

def function(x):

	t9 = x
	a6 = 3
	x = 6
	paths = []
	try:
		if a6 < 2:
			x = x*a6
			x = x+a6
			x = x-0
			paths.append(1)
		else:
			t9 = 4+a6
			x = x/x
			paths.append(2)
		if t9 < 0:
			x = 2+x
			x = x/6
			x = x+3
			paths.append(3)
		else:
			x = x-t9
			t9 = t9-a6
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