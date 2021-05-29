import numpy as np 

def function(x):

	s2 = x
	w1 = x
	paths = []
	try:
		if w1 < 0:
			x = 3/x
			s2 = s2*w1
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if s2 <= 8:
			w1 = 3/w1
			paths.append(3)
		else:
			x = x+0
			s2 = 9/s2
			w1 = w1+9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))