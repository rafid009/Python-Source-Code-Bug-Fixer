import numpy as np 

def function(x):

	h9 = 0
	t5 = 0
	paths = []
	try:
		if h9 < 5:
			t5 = 2-0
			paths.append(1)
		else:
			t5 = t5/x
			t5 = t5-9
			paths.append(2)
		if t5 <= 5:
			t5 = t5*h9
			paths.append(3)
		else:
			h9 = x*4
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