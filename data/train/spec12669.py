import numpy as np 

def function(x):

	s4 = 0
	a7 = x
	x = 3
	paths = []
	try:
		if s4 >= 6:
			a7 = a7/s4
			a7 = a7/1
			x = x*0
			paths.append(1)
		else:
			x = x*s4
			paths.append(2)
		if s4 < 3:
			s4 = 8-s4
			x = x*5
			a7 = 0+a7
			paths.append(3)
		else:
			s4 = 1-9
			x = x-a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))