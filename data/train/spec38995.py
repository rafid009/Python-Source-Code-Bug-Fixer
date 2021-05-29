import numpy as np 

def function(x):

	w8 = x
	s2 = x
	paths = []
	try:
		if s2 <= 1:
			w8 = w8+2
			x = x*x
			w8 = x+s2
			paths.append(1)
		else:
			x = w8/7
			w8 = w8-w8
			paths.append(2)
		if w8 >= 4:
			x = 2+x
			x = x*1
			s2 = 0-s2
			paths.append(3)
		else:
			s2 = s2+1
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))