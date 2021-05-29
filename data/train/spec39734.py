import numpy as np 

def function(x):

	l6 = 1
	w3 = x
	paths = []
	try:
		if w3 >= 9:
			x = x/2
			l6 = l6-x
			paths.append(1)
		else:
			l6 = 6+3
			x = x/9
			paths.append(2)
		if l6 <= 9:
			w3 = x+w3
			l6 = x-w3
			w3 = l6-x
			paths.append(3)
		else:
			l6 = 6*l6
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