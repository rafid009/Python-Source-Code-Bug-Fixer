import numpy as np 

def function(x):

	s5 = 7
	r5 = 0
	x = x
	paths = []
	try:
		if x <= 3:
			s5 = x-x
			paths.append(1)
		else:
			r5 = 1/6
			r5 = r5/r5
			s5 = x*x
			paths.append(2)
		if x >= 3:
			s5 = 2*x
			s5 = s5+5
			r5 = r5/x
			paths.append(3)
		else:
			s5 = 9+s5
			s5 = s5+3
			r5 = r5-5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))