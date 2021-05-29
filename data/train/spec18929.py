import numpy as np 

def function(x):

	s9 = x
	z7 = 5
	paths = []
	try:
		if z7 >= 6:
			z7 = 5+5
			paths.append(1)
		else:
			s9 = 6+x
			x = x+2
			x = x/9
			paths.append(2)
		if z7 < 3:
			s9 = s9/x
			z7 = x+1
			s9 = 6/s9
			paths.append(3)
		else:
			z7 = z7-z7
			x = 0+x
			x = x+2
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		z7 = s9**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))