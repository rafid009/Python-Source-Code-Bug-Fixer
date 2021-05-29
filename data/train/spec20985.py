import numpy as np 

def function(x):

	r4 = x
	o2 = 1
	paths = []
	try:
		if o2 <= 3:
			o2 = r4/o2
			x = x+0
			x = 3/8
			paths.append(1)
		else:
			x = 9+x
			r4 = r4*r4
			r4 = r4+5
			paths.append(2)
		if o2 >= 3:
			r4 = r4-1
			o2 = r4*o2
			o2 = 8+o2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))