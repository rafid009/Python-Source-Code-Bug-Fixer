import numpy as np 

def function(x):

	d8 = 2
	r0 = x
	paths = []
	try:
		if x < 5:
			d8 = d8*8
			d8 = d8*3
			paths.append(1)
		else:
			x = d8+x
			paths.append(2)
		if d8 <= 7:
			d8 = 0/d8
			x = x-6
			paths.append(3)
		else:
			d8 = r0-d8
			r0 = d8+x
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		r0 = d8**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))