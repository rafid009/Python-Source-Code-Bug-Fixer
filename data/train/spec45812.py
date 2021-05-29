import numpy as np 

def function(x):

	a5 = 9
	s4 = x
	paths = []
	try:
		if a5 <= 7:
			x = x*3
			x = x-7
			x = x+5
			paths.append(1)
		else:
			a5 = x+2
			s4 = 6*a5
			paths.append(2)
		if a5 >= 5:
			s4 = 8+s4
			s4 = 5*2
			paths.append(3)
		else:
			a5 = a5*2
			s4 = x-7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		s4 = a5**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))