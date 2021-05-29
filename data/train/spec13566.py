import numpy as np 

def function(x):

	h3 = x
	w3 = 0
	paths = []
	try:
		if h3 >= 4:
			h3 = x/h3
			paths.append(1)
		else:
			x = x*w3
			w3 = w3*2
			paths.append(2)
		if w3 >= 7:
			w3 = 6+h3
			x = 2+x
			paths.append(3)
		else:
			x = x*x
			h3 = h3+9
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