import numpy as np 

def function(x):

	l0 = 5
	s4 = 4
	paths = []
	try:
		if l0 <= 3:
			s4 = x*6
			paths.append(1)
		else:
			x = x+l0
			s4 = s4*x
			l0 = l0*7
			paths.append(2)
		if l0 > 0:
			s4 = x/1
			x = 8*x
			l0 = l0/2
			paths.append(3)
		else:
			s4 = s4*s4
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		l0 = s4**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))