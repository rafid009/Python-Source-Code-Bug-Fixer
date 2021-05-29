import numpy as np 

def function(x):

	w9 = 2
	t3 = x
	paths = []
	try:
		if x >= 1:
			w9 = w9/8
			x = x+6
			paths.append(1)
		else:
			x = x-w9
			w9 = w9/9
			paths.append(2)
		if t3 < 1:
			w9 = 4+w9
			paths.append(3)
		else:
			t3 = t3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))