import numpy as np 

def function(x):

	s5 = x
	x6 = 5
	paths = []
	try:
		if x6 < 1:
			x = 4+x
			s5 = s5-5
			x6 = x6+2
			paths.append(1)
		else:
			s5 = 2+s5
			s5 = s5-6
			paths.append(2)
		if x > 6:
			s5 = s5+4
			s5 = x+2
			x = 1-x
			paths.append(3)
		else:
			x6 = 1/s5
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))