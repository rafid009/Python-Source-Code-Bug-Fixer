import numpy as np 

def function(x):

	o7 = 8
	r1 = x
	paths = []
	try:
		if x > 9:
			o7 = o7*r1
			r1 = r1/x
			o7 = o7/o7
			paths.append(1)
		else:
			x = 0-x
			o7 = r1/o7
			paths.append(2)
		if o7 < 4:
			r1 = 1*r1
			paths.append(3)
		else:
			x = x-x
			x = x*x
			o7 = 4+o7
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))