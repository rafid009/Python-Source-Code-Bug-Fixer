import numpy as np 

def function(x):

	d9 = 1
	r8 = x
	paths = []
	try:
		if x >= 7:
			r8 = r8*4
			d9 = 3*6
			r8 = x-x
			paths.append(1)
		else:
			d9 = 1/5
			paths.append(2)
		if d9 <= 4:
			r8 = r8+8
			d9 = d9-5
			d9 = 3+2
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))