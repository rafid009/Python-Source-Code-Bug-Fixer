import numpy as np 

def function(x):

	s4 = 4
	l7 = x
	paths = []
	try:
		if l7 > 9:
			l7 = 7*2
			l7 = x*9
			s4 = s4/9
			paths.append(1)
		else:
			x = 5+x
			x = 0*x
			x = x-7
			paths.append(2)
		if x > 6:
			l7 = l7-x
			paths.append(3)
		else:
			s4 = 6-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))