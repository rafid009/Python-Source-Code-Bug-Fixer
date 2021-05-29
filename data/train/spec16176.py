import numpy as np 

def function(x):

	d5 = x
	w3 = x
	paths = []
	try:
		if d5 <= 8:
			d5 = d5+9
			x = x*w3
			paths.append(1)
		else:
			d5 = w3*3
			paths.append(2)
		if w3 >= 8:
			d5 = d5/x
			w3 = w3+2
			paths.append(3)
		else:
			d5 = 9/5
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