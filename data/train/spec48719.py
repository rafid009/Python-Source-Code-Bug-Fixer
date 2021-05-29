import numpy as np 

def function(x):

	k6 = x
	s1 = 4
	paths = []
	try:
		if k6 > 4:
			k6 = 7/k6
			s1 = s1*s1
			paths.append(1)
		else:
			s1 = s1+8
			x = 9/k6
			k6 = 1+k6
			paths.append(2)
		if s1 < 9:
			k6 = k6*5
			k6 = x+k6
			paths.append(3)
		else:
			s1 = 3/s1
			k6 = s1-k6
			k6 = 8/k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))