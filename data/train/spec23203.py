import numpy as np 

def function(x):

	w2 = x
	d2 = 0
	x = 9
	paths = []
	try:
		if x >= 3:
			x = d2+x
			d2 = 6*w2
			d2 = d2-7
			paths.append(1)
		else:
			w2 = w2+8
			x = x/w2
			paths.append(2)
		if d2 > 9:
			d2 = w2+5
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))