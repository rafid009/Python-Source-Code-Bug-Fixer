import numpy as np 

def function(x):

	w9 = 6
	t8 = 9
	paths = []
	try:
		if x <= 1:
			t8 = w9*x
			w9 = x-x
			t8 = t8+0
			paths.append(1)
		else:
			w9 = w9/9
			t8 = 1*x
			x = x/t8
			paths.append(2)
		if t8 < 1:
			t8 = t8-x
			t8 = t8-8
			paths.append(3)
		else:
			w9 = 4/3
			x = x/4
			w9 = w9+w9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))