import numpy as np 

def function(x):

	h6 = x
	w1 = 9
	paths = []
	try:
		if x >= 4:
			h6 = w1*h6
			paths.append(1)
		else:
			h6 = 6/h6
			h6 = 3*0
			h6 = x*4
			paths.append(2)
		if x > 7:
			x = 2*0
			h6 = 6-9
			paths.append(3)
		else:
			w1 = 7-9
			h6 = h6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))