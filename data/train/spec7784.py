import numpy as np 

def function(x):

	y7 = x
	o4 = x
	paths = []
	try:
		if o4 < 2:
			x = x-0
			o4 = o4*8
			paths.append(1)
		else:
			x = 9*x
			x = x*0
			x = x*x
			paths.append(2)
		if o4 >= 7:
			y7 = 4-y7
			y7 = x*4
			paths.append(3)
		else:
			o4 = o4/2
			y7 = 3*x
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