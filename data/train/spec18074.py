import numpy as np 

def function(x):

	s8 = x
	w1 = 8
	paths = []
	try:
		if s8 >= 1:
			w1 = s8+x
			x = x+5
			x = 2+s8
			paths.append(1)
		else:
			w1 = w1*3
			paths.append(2)
		if s8 <= 2:
			w1 = w1*x
			s8 = 5+s8
			paths.append(3)
		else:
			x = 8*5
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