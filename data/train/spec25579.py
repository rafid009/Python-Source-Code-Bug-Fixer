import numpy as np 

def function(x):

	s7 = 2
	k6 = x
	paths = []
	try:
		if k6 >= 4:
			x = 1*x
			x = k6*x
			x = x-8
			paths.append(1)
		else:
			x = 4*6
			x = x/2
			x = 5-x
			paths.append(2)
		if k6 <= 2:
			k6 = 7+k6
			x = 8*0
			k6 = k6/6
			paths.append(3)
		else:
			s7 = s7/s7
			s7 = s7+s7
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		s7 = k6**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))