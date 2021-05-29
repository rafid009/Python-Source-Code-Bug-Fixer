import numpy as np 

def function(x):

	w7 = 3
	t9 = 4
	paths = []
	try:
		if w7 < 4:
			w7 = w7-w7
			w7 = 5-5
			w7 = 1/t9
			paths.append(1)
		else:
			t9 = x+t9
			w7 = w7-4
			x = x/1
			paths.append(2)
		if x >= 9:
			x = x-3
			paths.append(3)
		else:
			w7 = 9*w7
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))