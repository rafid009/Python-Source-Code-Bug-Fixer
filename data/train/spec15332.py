import numpy as np 

def function(x):

	h4 = 6
	w3 = x
	paths = []
	try:
		if x > 4:
			x = x*1
			h4 = h4-7
			x = 5-6
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if h4 >= 3:
			h4 = x*h4
			w3 = w3*h4
			h4 = h4*w3
			paths.append(3)
		else:
			w3 = w3*h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		w3 = h4**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))