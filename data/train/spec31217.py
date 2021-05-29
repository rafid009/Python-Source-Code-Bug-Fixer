import numpy as np 

def function(x):

	x5 = x
	t9 = x
	paths = []
	try:
		if x5 <= 5:
			x5 = x5/3
			t9 = t9*t9
			t9 = 2-t9
			paths.append(1)
		else:
			x5 = 2+t9
			x5 = t9-x5
			paths.append(2)
		if t9 <= 8:
			x = x+7
			t9 = 5*t9
			x5 = x5/x
			paths.append(3)
		else:
			t9 = 2-t9
			x = 3+x
			x = x/9
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