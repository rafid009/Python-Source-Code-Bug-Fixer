import numpy as np 

def function(x):

	s4 = x
	r8 = 2
	paths = []
	try:
		if r8 >= 3:
			x = 9+0
			x = x*8
			x = x*x
			paths.append(1)
		else:
			x = r8-x
			s4 = 4-s4
			x = x/4
			paths.append(2)
		if r8 <= 8:
			r8 = 4+3
			paths.append(3)
		else:
			s4 = s4+6
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