import numpy as np 

def function(x):

	w6 = x
	h3 = 5
	paths = []
	try:
		if w6 > 5:
			w6 = w6*w6
			x = x*x
			paths.append(1)
		else:
			h3 = 4*x
			w6 = w6-w6
			paths.append(2)
		if x <= 9:
			h3 = h3/4
			paths.append(3)
		else:
			h3 = h3+w6
			w6 = 7*w6
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