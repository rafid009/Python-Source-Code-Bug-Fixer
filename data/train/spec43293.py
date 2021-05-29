import numpy as np 

def function(x):

	w3 = x
	d1 = x
	paths = []
	try:
		if d1 >= 6:
			w3 = 8+d1
			d1 = d1+8
			d1 = d1-5
			paths.append(1)
		else:
			x = w3-4
			w3 = d1*d1
			w3 = 4-5
			paths.append(2)
		if d1 < 5:
			d1 = w3*1
			paths.append(3)
		else:
			x = x/7
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