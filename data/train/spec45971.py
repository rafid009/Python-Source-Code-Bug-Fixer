import numpy as np 

def function(x):

	o4 = x
	r9 = x
	paths = []
	try:
		if r9 < 5:
			x = 2*0
			paths.append(1)
		else:
			o4 = o4+3
			x = x+3
			paths.append(2)
		if x >= 8:
			r9 = 0/2
			paths.append(3)
		else:
			o4 = o4*4
			r9 = r9/3
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))