import numpy as np 

def function(x):

	d2 = 1
	r7 = x
	paths = []
	try:
		if r7 <= 0:
			d2 = 2/x
			d2 = d2-x
			paths.append(1)
		else:
			x = x*d2
			r7 = r7+r7
			d2 = d2/r7
			paths.append(2)
		if r7 > 3:
			r7 = r7-7
			paths.append(3)
		else:
			r7 = 4-d2
			r7 = r7*r7
			r7 = 6/2
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))