import numpy as np 

def function(x):

	w5 = 7
	t8 = x
	paths = []
	try:
		if x > 5:
			t8 = 2-2
			x = 3/9
			t8 = t8-4
			paths.append(1)
		else:
			t8 = t8-0
			paths.append(2)
		if x > 4:
			t8 = t8+t8
			w5 = x+x
			x = x-7
			paths.append(3)
		else:
			t8 = t8-t8
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