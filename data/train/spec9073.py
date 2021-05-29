import numpy as np 

def function(x):

	p3 = x
	w3 = x
	paths = []
	try:
		if x >= 9:
			x = w3*2
			w3 = w3/8
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if w3 >= 4:
			w3 = p3*8
			paths.append(3)
		else:
			p3 = p3/x
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w3 = w3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))