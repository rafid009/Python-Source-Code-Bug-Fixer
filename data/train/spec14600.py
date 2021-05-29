import numpy as np 

def function(x):

	w6 = x
	d2 = x
	paths = []
	try:
		if d2 < 6:
			d2 = 7+x
			d2 = 0+x
			d2 = 1-0
			paths.append(1)
		else:
			w6 = w6+3
			w6 = d2-2
			x = x-7
			paths.append(2)
		if w6 < 8:
			x = 8-0
			d2 = d2-6
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		w6 = d2**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))