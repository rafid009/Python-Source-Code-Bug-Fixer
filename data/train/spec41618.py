import numpy as np 

def function(x):

	s7 = 8
	a2 = 7
	paths = []
	try:
		if s7 >= 6:
			x = x-1
			s7 = x*2
			x = x-x
			paths.append(1)
		else:
			a2 = a2/x
			s7 = 4*s7
			a2 = x*6
			paths.append(2)
		if s7 >= 5:
			a2 = a2*a2
			paths.append(3)
		else:
			s7 = s7*3
			x = x+9
			a2 = a2-x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		a2 = s7**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))