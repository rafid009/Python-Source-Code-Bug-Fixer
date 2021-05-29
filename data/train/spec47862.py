import numpy as np 

def function(x):

	f9 = x
	r1 = 8
	x = 4
	paths = []
	try:
		if x <= 9:
			r1 = 8*r1
			x = 2*x
			paths.append(1)
		else:
			x = f9-x
			paths.append(2)
		if x <= 7:
			r1 = 3-x
			paths.append(3)
		else:
			r1 = 3/f9
			x = x-0
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))