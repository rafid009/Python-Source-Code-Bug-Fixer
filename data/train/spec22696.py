import numpy as np 

def function(x):

	s1 = 8
	w7 = x
	paths = []
	try:
		if w7 >= 1:
			s1 = s1*2
			paths.append(1)
		else:
			w7 = 3+x
			s1 = s1*s1
			paths.append(2)
		if w7 <= 6:
			x = 0-3
			s1 = s1*s1
			w7 = 1-w7
			paths.append(3)
		else:
			w7 = w7*6
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))