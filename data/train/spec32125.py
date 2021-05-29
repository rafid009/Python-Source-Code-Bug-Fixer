import numpy as np 

def function(x):

	d4 = x
	r0 = 5
	paths = []
	try:
		if d4 < 7:
			x = 2+x
			paths.append(1)
		else:
			r0 = 7/r0
			r0 = r0/3
			d4 = d4*r0
			paths.append(2)
		if r0 > 1:
			r0 = r0-2
			r0 = d4*r0
			x = x/r0
			paths.append(3)
		else:
			x = x+7
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))