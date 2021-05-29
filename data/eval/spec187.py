import numpy as np 

def function(x):

	w6 = x
	h7 = x
	paths = []
	try:
		if x >= 4:
			w6 = w6+0
			x = x/2
			h7 = 5*h7
			paths.append(1)
		else:
			w6 = w6*2
			w6 = 7+w6
			h7 = w6-w6
			paths.append(2)
		if x <= 4:
			w6 = w6+w6
			h7 = h7+3
			paths.append(3)
		else:
			w6 = w6/w6
			w6 = h7+h7
			x = x-x
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