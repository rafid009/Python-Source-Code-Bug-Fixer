import numpy as np 

def function(x):

	b6 = x
	w3 = x
	paths = []
	try:
		if w3 > 6:
			w3 = w3-w3
			w3 = w3*2
			paths.append(1)
		else:
			w3 = w3*3
			paths.append(2)
		if b6 < 3:
			b6 = 4*5
			b6 = b6-w3
			x = x*b6
			paths.append(3)
		else:
			x = x/8
			b6 = 8-w3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))