import numpy as np 

def function(x):

	d2 = 3
	r3 = x
	paths = []
	try:
		if x < 6:
			d2 = 1*d2
			paths.append(1)
		else:
			x = 4-x
			r3 = 5*d2
			paths.append(2)
		if r3 > 2:
			r3 = r3*8
			r3 = 8+r3
			paths.append(3)
		else:
			d2 = 8-d2
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))