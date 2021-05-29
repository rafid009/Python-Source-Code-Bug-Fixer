import numpy as np 

def function(x):

	t4 = x
	l9 = x
	paths = []
	try:
		if l9 < 3:
			l9 = 6*9
			paths.append(1)
		else:
			t4 = 0-t4
			t4 = 0/5
			l9 = l9+x
			paths.append(2)
		if t4 < 3:
			x = l9/x
			paths.append(3)
		else:
			t4 = 3*4
			l9 = l9/x
			l9 = t4-l9
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