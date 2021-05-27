import numpy as np 

def function(x):

	s5 = x
	o0 = x
	paths = []
	try:
		if s5 > 7:
			o0 = 6/2
			s5 = 7+s5
			paths.append(1)
		else:
			x = s5*3
			paths.append(2)
		if o0 > 8:
			o0 = o0+o0
			paths.append(3)
		else:
			s5 = s5-o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))