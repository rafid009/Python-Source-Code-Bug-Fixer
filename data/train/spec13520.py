import numpy as np 

def function(x):

	t5 = 7
	h7 = 4
	paths = []
	try:
		if x >= 0:
			h7 = h7-4
			paths.append(1)
		else:
			t5 = 8/t5
			x = x/x
			paths.append(2)
		if x >= 9:
			x = 1-2
			t5 = 1*3
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))