import numpy as np 

def function(x):

	w9 = 6
	d2 = x
	paths = []
	try:
		if w9 > 8:
			w9 = w9/d2
			d2 = 5*3
			d2 = d2-5
			paths.append(1)
		else:
			x = 6/3
			paths.append(2)
		if x >= 4:
			w9 = w9/w9
			x = 4*1
			paths.append(3)
		else:
			w9 = 0/x
			d2 = 7+d2
			d2 = d2+9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))