import numpy as np 

def function(x):

	d1 = x
	r1 = x
	paths = []
	try:
		if x >= 5:
			r1 = 4*r1
			r1 = 1-r1
			r1 = 7+r1
			paths.append(1)
		else:
			x = r1-2
			paths.append(2)
		if x >= 4:
			x = 2+x
			x = 4/d1
			paths.append(3)
		else:
			d1 = d1/r1
			r1 = 9/3
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		d1 = r1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))