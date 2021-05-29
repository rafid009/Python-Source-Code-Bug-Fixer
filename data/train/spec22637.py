import numpy as np 

def function(x):

	s9 = 6
	w1 = 9
	x = x
	paths = []
	try:
		if s9 <= 3:
			s9 = s9-s9
			paths.append(1)
		else:
			w1 = w1/8
			paths.append(2)
		if x >= 9:
			s9 = 5-s9
			x = x/6
			paths.append(3)
		else:
			x = w1/x
			w1 = w1-x
			x = 6/9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))