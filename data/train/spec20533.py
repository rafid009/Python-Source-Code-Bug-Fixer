import numpy as np 

def function(x):

	w1 = x
	h2 = x
	paths = []
	try:
		if w1 < 0:
			h2 = 1+h2
			h2 = h2+6
			h2 = h2/4
			paths.append(1)
		else:
			w1 = w1*6
			x = x+7
			paths.append(2)
		if w1 < 7:
			w1 = w1*6
			h2 = h2*2
			paths.append(3)
		else:
			w1 = w1/w1
			h2 = h2+3
			h2 = w1/h2
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