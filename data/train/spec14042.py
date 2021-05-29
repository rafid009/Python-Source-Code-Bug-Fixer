import numpy as np 

def function(x):

	s4 = x
	w3 = x
	paths = []
	try:
		if s4 < 2:
			s4 = s4*2
			w3 = s4+w3
			w3 = w3*x
			paths.append(1)
		else:
			x = 0/x
			x = 3*x
			x = w3-6
			paths.append(2)
		if s4 > 6:
			s4 = s4-6
			paths.append(3)
		else:
			s4 = s4*1
			w3 = 3+w3
			x = 5+0
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))