import numpy as np 

def function(x):

	w4 = 2
	s7 = x
	paths = []
	try:
		if x < 2:
			w4 = w4+s7
			paths.append(1)
		else:
			x = 0/x
			x = 6*1
			paths.append(2)
		if w4 < 6:
			s7 = s7*2
			paths.append(3)
		else:
			w4 = w4/7
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))