import numpy as np 

def function(x):

	r3 = x
	d2 = x
	paths = []
	try:
		if r3 > 2:
			r3 = x+1
			d2 = 9+r3
			paths.append(1)
		else:
			r3 = r3-4
			r3 = r3/3
			d2 = 0-5
			paths.append(2)
		if x > 6:
			r3 = 5-r3
			x = x-r3
			paths.append(3)
		else:
			x = 1*x
			x = 9*0
			d2 = 3*d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		r3 = d2**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))