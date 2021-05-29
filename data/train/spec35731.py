import numpy as np 

def function(x):

	a0 = x
	s5 = 1
	x = x
	paths = []
	try:
		if a0 < 4:
			s5 = a0-0
			a0 = 9-a0
			paths.append(1)
		else:
			a0 = a0/2
			x = 1*x
			paths.append(2)
		if x >= 8:
			x = x-x
			x = 8/2
			s5 = x*3
			paths.append(3)
		else:
			s5 = s5+s5
			x = 1+x
			s5 = s5/a0
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