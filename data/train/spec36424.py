import numpy as np 

def function(x):

	r3 = 8
	d9 = x
	paths = []
	try:
		if d9 >= 8:
			d9 = 0/x
			x = 2*r3
			r3 = r3/4
			paths.append(1)
		else:
			x = 4-x
			d9 = d9/d9
			d9 = 7*d9
			paths.append(2)
		if d9 < 5:
			d9 = x-1
			paths.append(3)
		else:
			r3 = x*5
			r3 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))