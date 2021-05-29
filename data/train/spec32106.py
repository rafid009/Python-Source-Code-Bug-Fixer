import numpy as np 

def function(x):

	b8 = 8
	w3 = x
	paths = []
	try:
		if b8 >= 1:
			x = w3-x
			paths.append(1)
		else:
			x = 7-x
			w3 = w3/6
			paths.append(2)
		if w3 >= 8:
			b8 = x/w3
			w3 = w3+w3
			w3 = b8/w3
			paths.append(3)
		else:
			b8 = b8-5
			x = b8+4
			b8 = b8*4
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		b8 = w3**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))