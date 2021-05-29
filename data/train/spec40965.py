import numpy as np 

def function(x):

	d6 = 7
	r2 = x
	paths = []
	try:
		if r2 < 9:
			r2 = 9-2
			d6 = x+r2
			paths.append(1)
		else:
			d6 = d6*8
			d6 = 2*d6
			paths.append(2)
		if d6 >= 2:
			d6 = x-d6
			d6 = d6*d6
			r2 = 9-7
			paths.append(3)
		else:
			r2 = 7*8
			d6 = 4*d6
			r2 = x+6
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))