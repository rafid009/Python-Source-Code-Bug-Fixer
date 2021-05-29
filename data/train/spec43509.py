import numpy as np 

def function(x):

	t3 = x
	h2 = x
	paths = []
	try:
		if t3 >= 5:
			x = 3/7
			paths.append(1)
		else:
			x = 4/x
			t3 = 7*6
			t3 = t3-2
			paths.append(2)
		if t3 <= 8:
			x = x/x
			h2 = h2*h2
			x = 5*9
			paths.append(3)
		else:
			t3 = t3-3
			t3 = t3/1
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))