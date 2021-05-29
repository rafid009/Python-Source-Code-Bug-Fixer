import numpy as np 

def function(x):

	s4 = x
	r0 = x
	paths = []
	try:
		if r0 > 1:
			r0 = r0*4
			paths.append(1)
		else:
			s4 = 7+s4
			paths.append(2)
		if r0 >= 0:
			r0 = 6+r0
			r0 = r0+s4
			paths.append(3)
		else:
			s4 = s4*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))