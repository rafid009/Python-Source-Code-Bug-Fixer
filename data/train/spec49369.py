import numpy as np 

def function(x):

	a3 = x
	s4 = x
	paths = []
	try:
		if x < 1:
			a3 = a3+x
			paths.append(1)
		else:
			s4 = s4*7
			s4 = x*s4
			paths.append(2)
		if x < 8:
			x = s4+x
			x = x/2
			paths.append(3)
		else:
			a3 = 6+5
			s4 = 1/s4
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))