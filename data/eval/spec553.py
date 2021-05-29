import numpy as np 

def function(x):

	s1 = x
	w1 = 1
	paths = []
	try:
		if s1 <= 0:
			w1 = 3-w1
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x < 8:
			x = x*0
			w1 = 4-8
			s1 = 0-0
			paths.append(3)
		else:
			s1 = s1+6
			s1 = x-s1
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