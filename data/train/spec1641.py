import numpy as np 

def function(x):

	d2 = x
	h7 = 0
	paths = []
	try:
		if h7 > 2:
			d2 = 2+8
			d2 = 3/d2
			paths.append(1)
		else:
			x = h7*0
			d2 = d2-h7
			paths.append(2)
		if d2 <= 0:
			x = x*4
			d2 = d2+0
			x = 6*x
			paths.append(3)
		else:
			d2 = x/d2
			x = 9-7
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