import numpy as np 

def function(x):

	h8 = 4
	w6 = x
	paths = []
	try:
		if w6 >= 1:
			h8 = w6*0
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if w6 > 9:
			x = 7-x
			paths.append(3)
		else:
			h8 = 0-h8
			w6 = h8+w6
			h8 = 3+h8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))