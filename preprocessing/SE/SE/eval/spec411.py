import numpy as np 

def function(x):

	w6 = x
	s2 = 8
	paths = []
	try:
		if s2 >= 6:
			x = x/4
			x = x-s2
			paths.append(1)
		else:
			w6 = w6-8
			s2 = s2*1
			paths.append(2)
		if w6 > 6:
			x = w6+6
			paths.append(3)
		else:
			s2 = 3*w6
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		w6 = s2**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))