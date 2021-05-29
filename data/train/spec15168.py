import numpy as np 

def function(x):

	w5 = x
	d4 = 1
	paths = []
	try:
		if x > 5:
			w5 = w5*8
			paths.append(1)
		else:
			d4 = d4*2
			d4 = x+d4
			w5 = 7+4
			paths.append(2)
		if w5 > 7:
			x = 8+6
			x = 1+4
			w5 = d4+6
			paths.append(3)
		else:
			x = x*1
			w5 = 0-w5
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		w5 = d4**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))