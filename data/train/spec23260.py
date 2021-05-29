import numpy as np 

def function(x):

	w1 = 3
	s6 = 2
	paths = []
	try:
		if x >= 1:
			s6 = 1/s6
			w1 = w1/s6
			s6 = 5/s6
			paths.append(1)
		else:
			w1 = 7-x
			paths.append(2)
		if x > 8:
			s6 = 9/s6
			s6 = 2-w1
			x = s6-x
			paths.append(3)
		else:
			s6 = 1*w1
			s6 = s6+x
			w1 = 3+w1
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		w1 = s6**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))