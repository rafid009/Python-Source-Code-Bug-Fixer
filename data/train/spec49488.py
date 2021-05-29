import numpy as np 

def function(x):

	t2 = 3
	w9 = x
	paths = []
	try:
		if x >= 6:
			w9 = w9+7
			t2 = t2/w9
			paths.append(1)
		else:
			w9 = w9+w9
			paths.append(2)
		if x < 3:
			w9 = 2/w9
			w9 = t2+t2
			paths.append(3)
		else:
			w9 = w9/t2
			t2 = 2/t2
			t2 = 3-t2
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