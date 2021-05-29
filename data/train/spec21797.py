import numpy as np 

def function(x):

	d6 = 0
	r8 = 2
	paths = []
	try:
		if d6 >= 1:
			r8 = 1+5
			r8 = d6-d6
			r8 = 5/d6
			paths.append(1)
		else:
			r8 = 4*9
			paths.append(2)
		if x <= 3:
			d6 = r8+3
			paths.append(3)
		else:
			x = x-9
			r8 = r8*d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))