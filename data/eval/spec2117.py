import numpy as np 

def function(x):

	s2 = x
	paths = []
	try:
		if s2 > 4:
			x = 8*x
			s2 = 5*x
			paths.append(1)
		else:
			x = 6/s2
			paths.append(2)
		if x <= 5:
			x = x/4
			x = 0+0
			s2 = s2/5
			paths.append(3)
		else:
			x = 4*0
			x = x+9
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))