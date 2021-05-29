import numpy as np 

def function(x):

	h6 = x
	t5 = 3
	paths = []
	try:
		if x <= 5:
			t5 = 8/t5
			paths.append(1)
		else:
			t5 = 5-2
			t5 = t5/2
			paths.append(2)
		if h6 >= 6:
			x = x*7
			x = 6/x
			x = 4-x
			paths.append(3)
		else:
			t5 = t5+6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))