import numpy as np 

def function(x):

	s9 = x
	w5 = x
	paths = []
	try:
		if w5 >= 0:
			s9 = 7-2
			paths.append(1)
		else:
			s9 = x-8
			x = x/7
			x = x/4
			paths.append(2)
		if x <= 0:
			w5 = w5+s9
			x = 2/s9
			paths.append(3)
		else:
			x = x+5
			x = x-6
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		s9 = w5**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))