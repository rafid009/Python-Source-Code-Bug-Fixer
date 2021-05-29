import numpy as np 

def function(x):

	o1 = x
	s9 = x
	paths = []
	try:
		if x >= 6:
			x = x-x
			paths.append(1)
		else:
			s9 = 1+s9
			s9 = s9*o1
			paths.append(2)
		if s9 <= 5:
			s9 = 5/s9
			x = x*s9
			s9 = s9*o1
			paths.append(3)
		else:
			o1 = o1-5
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))