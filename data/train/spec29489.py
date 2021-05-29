import numpy as np 

def function(x):

	s5 = 3
	w9 = x
	paths = []
	try:
		if w9 >= 9:
			s5 = 6-s5
			paths.append(1)
		else:
			w9 = 5/w9
			paths.append(2)
		if x >= 5:
			x = w9*7
			x = x/2
			paths.append(3)
		else:
			w9 = w9+1
			s5 = x*s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))