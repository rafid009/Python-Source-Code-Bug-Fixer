import numpy as np 

def function(x):

	d1 = x
	w7 = 0
	paths = []
	try:
		if d1 <= 2:
			d1 = d1-5
			paths.append(1)
		else:
			d1 = d1/5
			x = x+8
			paths.append(2)
		if x >= 1:
			w7 = w7-3
			d1 = d1-2
			x = 8*0
			paths.append(3)
		else:
			w7 = x+w7
			w7 = d1/w7
			x = d1/w7
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		w7 = d1**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))