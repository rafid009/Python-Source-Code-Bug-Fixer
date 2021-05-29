import numpy as np 

def function(x):

	w0 = x
	s6 = 9
	paths = []
	try:
		if s6 >= 4:
			x = s6-x
			x = x-6
			s6 = 2*s6
			paths.append(1)
		else:
			w0 = w0*6
			paths.append(2)
		if x >= 7:
			s6 = 7+w0
			paths.append(3)
		else:
			s6 = s6*3
			s6 = x+0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))