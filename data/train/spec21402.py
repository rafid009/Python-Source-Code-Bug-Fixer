import numpy as np 

def function(x):

	w3 = x
	p6 = x
	paths = []
	try:
		if p6 >= 5:
			w3 = w3+w3
			p6 = 1/p6
			paths.append(1)
		else:
			p6 = p6+0
			paths.append(2)
		if w3 < 4:
			x = x*6
			w3 = x-w3
			paths.append(3)
		else:
			w3 = w3*4
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