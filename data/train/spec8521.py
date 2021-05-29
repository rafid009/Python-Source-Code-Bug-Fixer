import numpy as np 

def function(x):

	w7 = x
	s6 = 1
	paths = []
	try:
		if x <= 1:
			w7 = 7*7
			s6 = s6*2
			paths.append(1)
		else:
			w7 = w7/3
			s6 = s6-w7
			paths.append(2)
		if x < 7:
			s6 = 6+4
			paths.append(3)
		else:
			x = 0/x
			w7 = x*5
			x = x+x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))