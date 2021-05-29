import numpy as np 

def function(x):

	a2 = x
	w3 = x
	paths = []
	try:
		if a2 < 1:
			a2 = 0+a2
			w3 = w3/1
			paths.append(1)
		else:
			x = x*5
			x = x+3
			paths.append(2)
		if w3 >= 7:
			w3 = 5+w3
			x = 9/x
			a2 = 4/a2
			paths.append(3)
		else:
			w3 = w3-5
			w3 = w3+0
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