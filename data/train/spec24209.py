import numpy as np 

def function(x):

	w3 = 0
	s2 = x
	paths = []
	try:
		if w3 <= 9:
			x = 3/8
			s2 = s2*8
			paths.append(1)
		else:
			x = 8+6
			w3 = w3+8
			x = 5-4
			paths.append(2)
		if w3 < 8:
			x = x+7
			x = 5+x
			w3 = w3-1
			paths.append(3)
		else:
			w3 = x*w3
			w3 = w3-s2
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		s2 = w3**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))