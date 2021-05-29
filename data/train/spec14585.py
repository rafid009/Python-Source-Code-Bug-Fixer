import numpy as np 

def function(x):

	l6 = x
	w3 = x
	paths = []
	try:
		if w3 >= 9:
			w3 = w3/2
			paths.append(1)
		else:
			x = 2+5
			l6 = l6*8
			paths.append(2)
		if w3 > 4:
			l6 = l6/x
			x = x*3
			l6 = l6-l6
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))