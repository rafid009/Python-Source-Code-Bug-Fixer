import numpy as np 

def function(x):

	l6 = x
	s1 = 5
	paths = []
	try:
		if l6 >= 1:
			l6 = l6*7
			l6 = l6-4
			l6 = l6-8
			paths.append(1)
		else:
			l6 = l6/s1
			x = x/4
			s1 = l6*x
			paths.append(2)
		if x > 6:
			x = x+3
			paths.append(3)
		else:
			l6 = l6*0
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))