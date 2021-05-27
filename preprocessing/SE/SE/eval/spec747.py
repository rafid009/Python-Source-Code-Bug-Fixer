import numpy as np 

def function(x):

	s1 = 9
	w0 = x
	paths = []
	try:
		if w0 <= 5:
			w0 = 4-w0
			paths.append(1)
		else:
			w0 = w0-5
			x = 6*x
			s1 = s1+5
			paths.append(2)
		if w0 < 1:
			s1 = s1-9
			x = x+x
			x = 0/x
			paths.append(3)
		else:
			x = 1+s1
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))