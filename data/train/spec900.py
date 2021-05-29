import numpy as np 

def function(x):

	r2 = 5
	d2 = 6
	paths = []
	try:
		if r2 <= 0:
			r2 = 5-r2
			x = x/d2
			x = x+d2
			paths.append(1)
		else:
			r2 = r2+d2
			d2 = d2-6
			x = x-5
			paths.append(2)
		if r2 < 6:
			d2 = d2*8
			r2 = 5*8
			x = x*5
			paths.append(3)
		else:
			r2 = r2+0
			d2 = d2*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))