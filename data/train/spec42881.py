import numpy as np 

def function(x):

	s2 = 2
	w2 = 3
	paths = []
	try:
		if s2 > 0:
			w2 = w2-1
			paths.append(1)
		else:
			w2 = 2/w2
			w2 = 7/4
			s2 = 0*s2
			paths.append(2)
		if x >= 4:
			x = x/x
			w2 = 9-w2
			paths.append(3)
		else:
			s2 = 8+x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))