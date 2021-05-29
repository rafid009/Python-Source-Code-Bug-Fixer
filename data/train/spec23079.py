import numpy as np 

def function(x):

	s0 = x
	a9 = x
	paths = []
	try:
		if a9 > 7:
			a9 = x*x
			paths.append(1)
		else:
			s0 = s0-6
			s0 = s0+5
			x = s0/5
			paths.append(2)
		if a9 > 6:
			x = 6*x
			s0 = x+s0
			s0 = s0*2
			paths.append(3)
		else:
			a9 = 2+7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		a9 = s0**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))