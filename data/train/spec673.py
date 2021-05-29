import numpy as np 

def function(x):

	i0 = 5
	t2 = 3
	paths = []
	try:
		if t2 >= 3:
			x = x/5
			paths.append(1)
		else:
			i0 = i0-3
			paths.append(2)
		if i0 <= 5:
			x = x-3
			t2 = 2-1
			i0 = i0/i0
			paths.append(3)
		else:
			i0 = t2-9
			t2 = 1/t2
			x = 0-x
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