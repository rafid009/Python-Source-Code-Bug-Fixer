import numpy as np 

def function(x):

	s7 = x
	o4 = x
	paths = []
	try:
		if x >= 6:
			x = x-0
			s7 = x+s7
			o4 = x-5
			paths.append(1)
		else:
			o4 = x-3
			x = 8-o4
			x = x*2
			paths.append(2)
		if x > 6:
			x = x*8
			o4 = o4-4
			paths.append(3)
		else:
			s7 = 6-s7
			x = 6+x
			x = 4*x
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