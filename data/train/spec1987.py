import numpy as np 

def function(x):

	s2 = 3
	f2 = x
	x = x
	paths = []
	try:
		if f2 > 1:
			s2 = s2*6
			x = 4*x
			f2 = f2*5
			paths.append(1)
		else:
			s2 = s2-x
			f2 = 1-9
			x = 5+8
			paths.append(2)
		if f2 > 3:
			s2 = 1*f2
			s2 = 1+s2
			x = s2/f2
			paths.append(3)
		else:
			s2 = 3/4
			s2 = 1+f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))