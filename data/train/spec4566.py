import numpy as np 

def function(x):

	d5 = x
	r3 = 4
	paths = []
	try:
		if r3 <= 6:
			d5 = 1-8
			paths.append(1)
		else:
			x = 4-x
			x = r3*3
			paths.append(2)
		if x < 6:
			d5 = d5+8
			d5 = d5+r3
			d5 = 6*0
			paths.append(3)
		else:
			d5 = 4*d5
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