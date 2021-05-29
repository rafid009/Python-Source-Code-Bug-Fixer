import numpy as np 

def function(x):

	s1 = 8
	k6 = 6
	paths = []
	try:
		if s1 > 6:
			x = x+7
			k6 = k6/6
			s1 = 1/s1
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x < 8:
			s1 = x+s1
			paths.append(3)
		else:
			s1 = 3-8
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		k6 = s1**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))