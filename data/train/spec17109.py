import numpy as np 

def function(x):

	h1 = x
	t1 = x
	x = 1
	paths = []
	try:
		if t1 > 3:
			x = x-4
			h1 = 6*h1
			paths.append(1)
		else:
			x = 8+8
			t1 = x-t1
			paths.append(2)
		if x >= 7:
			x = 6-6
			t1 = t1*2
			paths.append(3)
		else:
			h1 = h1-1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))