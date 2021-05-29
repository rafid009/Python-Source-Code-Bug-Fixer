import numpy as np 

def function(x):

	r7 = x
	s1 = x
	paths = []
	try:
		if x < 5:
			s1 = 7+s1
			x = x*x
			r7 = s1*r7
			paths.append(1)
		else:
			x = x/3
			s1 = s1-s1
			paths.append(2)
		if r7 <= 2:
			x = 3/x
			x = x+s1
			x = 4-x
			paths.append(3)
		else:
			x = x/8
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))