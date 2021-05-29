import numpy as np 

def function(x):

	t9 = x
	h2 = x
	paths = []
	try:
		if h2 <= 6:
			t9 = t9*8
			paths.append(1)
		else:
			t9 = 2/9
			t9 = 9-6
			paths.append(2)
		if t9 <= 5:
			t9 = 2-t9
			paths.append(3)
		else:
			h2 = t9*2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))