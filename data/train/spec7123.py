import numpy as np 

def function(x):

	s9 = x
	w7 = x
	x = 9
	paths = []
	try:
		if x < 6:
			w7 = w7*s9
			paths.append(1)
		else:
			x = 7+x
			w7 = w7/s9
			paths.append(2)
		if x <= 0:
			w7 = x-w7
			x = 8/2
			x = 5-7
			paths.append(3)
		else:
			w7 = x-w7
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))