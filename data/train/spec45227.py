import numpy as np 

def function(x):

	t5 = 5
	w9 = 6
	paths = []
	try:
		if x >= 9:
			x = 9+4
			w9 = w9/w9
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if x < 5:
			t5 = t5*x
			x = x-4
			paths.append(3)
		else:
			w9 = 3+w9
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))