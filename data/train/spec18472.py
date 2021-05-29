import numpy as np 

def function(x):

	v5 = 6
	d2 = x
	paths = []
	try:
		if x >= 8:
			x = x+4
			d2 = d2/5
			paths.append(1)
		else:
			d2 = 2*d2
			v5 = x*v5
			v5 = 7-v5
			paths.append(2)
		if v5 >= 1:
			x = x-3
			paths.append(3)
		else:
			x = 4+5
			x = x-8
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		d2 = v5**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))