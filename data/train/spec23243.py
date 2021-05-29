import numpy as np 

def function(x):

	h2 = x
	w1 = x
	paths = []
	try:
		if x <= 5:
			x = x/x
			h2 = h2/6
			x = 2-1
			paths.append(1)
		else:
			x = 0/x
			w1 = w1-9
			paths.append(2)
		if w1 <= 1:
			x = 8+x
			w1 = w1-h2
			w1 = w1/3
			paths.append(3)
		else:
			x = 7*6
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))