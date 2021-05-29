import numpy as np 

def function(x):

	l2 = x
	w3 = 8
	paths = []
	try:
		if w3 > 1:
			l2 = l2/5
			w3 = w3*1
			paths.append(1)
		else:
			x = x/7
			l2 = l2+w3
			paths.append(2)
		if w3 > 0:
			w3 = 0/w3
			l2 = w3*4
			l2 = x+w3
			paths.append(3)
		else:
			x = l2+l2
			l2 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))