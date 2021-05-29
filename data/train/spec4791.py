import numpy as np 

def function(x):

	i0 = 7
	s5 = x
	paths = []
	try:
		if i0 < 6:
			s5 = s5*x
			paths.append(1)
		else:
			s5 = i0-i0
			s5 = 3-s5
			s5 = 7*0
			paths.append(2)
		if s5 >= 7:
			i0 = i0-0
			x = x+6
			paths.append(3)
		else:
			i0 = 7+i0
			x = x+s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))