import numpy as np 

def function(x):

	r8 = x
	d8 = x
	paths = []
	try:
		if x <= 6:
			d8 = d8-3
			paths.append(1)
		else:
			d8 = 2-r8
			d8 = 2*5
			d8 = d8*9
			paths.append(2)
		if r8 >= 4:
			r8 = 3*r8
			paths.append(3)
		else:
			r8 = 3+2
			r8 = 9/r8
			x = 7*7
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		r8 = d8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))