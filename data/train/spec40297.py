import numpy as np 

def function(x):

	w1 = 2
	h9 = x
	paths = []
	try:
		if h9 < 1:
			w1 = h9/7
			h9 = h9+8
			h9 = 6-7
			paths.append(1)
		else:
			h9 = w1*w1
			h9 = x/5
			paths.append(2)
		if x >= 6:
			x = x*w1
			x = w1+1
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))