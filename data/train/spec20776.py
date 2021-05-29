import numpy as np 

def function(x):

	w0 = 4
	s1 = x
	paths = []
	try:
		if s1 > 9:
			s1 = x*5
			x = x+9
			paths.append(1)
		else:
			w0 = s1+s1
			paths.append(2)
		if w0 <= 6:
			s1 = s1/8
			x = x-0
			paths.append(3)
		else:
			s1 = 9+6
			w0 = w0+9
			s1 = 1-x
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