import numpy as np 

def function(x):

	s9 = x
	l9 = 5
	paths = []
	try:
		if x > 3:
			l9 = l9/s9
			x = x+6
			paths.append(1)
		else:
			x = x*l9
			x = x+5
			s9 = s9-0
			paths.append(2)
		if l9 >= 8:
			x = 6+x
			l9 = s9/9
			l9 = 7/8
			paths.append(3)
		else:
			s9 = 7/s9
			s9 = s9-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))