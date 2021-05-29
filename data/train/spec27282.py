import numpy as np 

def function(x):

	a5 = x
	s5 = x
	x = x
	paths = []
	try:
		if s5 <= 1:
			x = a5-s5
			paths.append(1)
		else:
			x = x*a5
			paths.append(2)
		if s5 < 1:
			s5 = 9-s5
			s5 = x/2
			paths.append(3)
		else:
			a5 = 8*a5
			s5 = 5*0
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))