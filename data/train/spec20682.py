import numpy as np 

def function(x):

	r2 = 6
	d5 = x
	paths = []
	try:
		if x <= 6:
			r2 = 0*r2
			paths.append(1)
		else:
			r2 = 0*r2
			r2 = r2-8
			r2 = 7*r2
			paths.append(2)
		if r2 > 5:
			x = 1-x
			d5 = d5+8
			r2 = r2/7
			paths.append(3)
		else:
			x = x/d5
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))