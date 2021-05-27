import numpy as np 

def function(x):

	l0 = 5
	s4 = 9
	paths = []
	try:
		if l0 <= 4:
			s4 = s4+1
			x = x-6
			paths.append(1)
		else:
			l0 = l0*2
			paths.append(2)
		if s4 < 4:
			s4 = s4*0
			x = x*7
			paths.append(3)
		else:
			x = x-5
			l0 = 0-l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))