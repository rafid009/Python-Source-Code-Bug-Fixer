import numpy as np 

def function(x):

	w5 = x
	s9 = 2
	paths = []
	try:
		if w5 < 7:
			x = x-8
			paths.append(1)
		else:
			s9 = s9*8
			s9 = 9-s9
			paths.append(2)
		if w5 <= 7:
			x = x-3
			x = x/w5
			paths.append(3)
		else:
			s9 = s9*1
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))