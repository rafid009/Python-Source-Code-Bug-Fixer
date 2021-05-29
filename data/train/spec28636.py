import numpy as np 

def function(x):

	t8 = 7
	h1 = x
	paths = []
	try:
		if x < 3:
			x = x-6
			t8 = x+t8
			paths.append(1)
		else:
			t8 = 7-t8
			h1 = h1+0
			paths.append(2)
		if x >= 3:
			t8 = t8*x
			t8 = t8-x
			paths.append(3)
		else:
			t8 = 7*t8
			x = 1*x
			t8 = t8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))