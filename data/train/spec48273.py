import numpy as np 

def function(x):

	w1 = 8
	h0 = x
	paths = []
	try:
		if x > 1:
			w1 = 6+7
			w1 = 3/w1
			paths.append(1)
		else:
			w1 = w1+2
			w1 = 7-4
			h0 = h0+h0
			paths.append(2)
		if x <= 0:
			x = 0+x
			w1 = w1*h0
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		w1 = h0**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))