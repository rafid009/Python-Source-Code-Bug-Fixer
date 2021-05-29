import numpy as np 

def function(x):

	w2 = x
	s6 = 6
	paths = []
	try:
		if x >= 4:
			s6 = s6/s6
			w2 = 0-w2
			paths.append(1)
		else:
			s6 = s6+0
			w2 = w2-9
			paths.append(2)
		if w2 >= 1:
			x = 5+x
			x = s6-x
			paths.append(3)
		else:
			w2 = s6+w2
			w2 = w2/2
			s6 = s6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))