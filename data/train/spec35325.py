import numpy as np 

def function(x):

	r5 = 8
	s9 = x
	paths = []
	try:
		if s9 > 8:
			s9 = s9*2
			paths.append(1)
		else:
			x = 3+5
			r5 = r5-7
			x = 5*x
			paths.append(2)
		if x > 3:
			r5 = r5-3
			x = x+1
			x = 5+s9
			paths.append(3)
		else:
			r5 = 8*s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))