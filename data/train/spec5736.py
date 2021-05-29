import numpy as np 

def function(x):

	a0 = x
	s4 = x
	paths = []
	try:
		if s4 >= 5:
			s4 = s4+1
			s4 = 8+1
			paths.append(1)
		else:
			a0 = a0/9
			s4 = 4-s4
			a0 = 1*a0
			paths.append(2)
		if x > 2:
			s4 = 2+s4
			paths.append(3)
		else:
			s4 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))