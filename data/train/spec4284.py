import numpy as np 

def function(x):

	s1 = x
	w0 = 8
	paths = []
	try:
		if x >= 3:
			s1 = 6/s1
			paths.append(1)
		else:
			w0 = w0*2
			x = x/s1
			paths.append(2)
		if x > 7:
			w0 = 1+w0
			x = s1+0
			x = x/w0
			paths.append(3)
		else:
			s1 = s1-9
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))