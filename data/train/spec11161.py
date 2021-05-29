import numpy as np 

def function(x):

	d7 = x
	r7 = 8
	paths = []
	try:
		if d7 <= 1:
			d7 = d7-3
			x = 0/d7
			paths.append(1)
		else:
			x = 5+x
			x = x*2
			paths.append(2)
		if r7 < 1:
			r7 = x-x
			d7 = 7+d7
			d7 = 5*d7
			paths.append(3)
		else:
			x = x-7
			x = 1+x
			d7 = r7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))