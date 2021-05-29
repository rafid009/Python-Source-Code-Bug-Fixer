import numpy as np 

def function(x):

	h3 = x
	t3 = 5
	paths = []
	try:
		if h3 <= 1:
			x = x*4
			paths.append(1)
		else:
			h3 = x*5
			x = 8-5
			paths.append(2)
		if t3 <= 5:
			t3 = 9*t3
			paths.append(3)
		else:
			t3 = t3*x
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))