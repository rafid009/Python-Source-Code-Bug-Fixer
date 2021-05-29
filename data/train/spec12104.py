import numpy as np 

def function(x):

	a7 = 8
	h9 = x
	paths = []
	try:
		if x > 1:
			a7 = 9-7
			paths.append(1)
		else:
			x = a7+5
			paths.append(2)
		if h9 <= 7:
			a7 = 1+a7
			paths.append(3)
		else:
			a7 = a7-h9
			a7 = a7*2
			h9 = 8+x
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))