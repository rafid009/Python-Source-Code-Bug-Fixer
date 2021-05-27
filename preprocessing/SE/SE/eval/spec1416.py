import numpy as np 

def function(x):

	s1 = 4
	w2 = x
	paths = []
	try:
		if x > 5:
			w2 = w2+1
			w2 = 2*x
			w2 = 0*x
			paths.append(1)
		else:
			s1 = x-6
			paths.append(2)
		if w2 < 7:
			w2 = w2*7
			paths.append(3)
		else:
			x = w2-x
			x = 0-w2
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))