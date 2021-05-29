import numpy as np 

def function(x):

	s1 = x
	k6 = 1
	paths = []
	try:
		if k6 < 1:
			s1 = 4/s1
			k6 = k6/6
			k6 = 6/k6
			paths.append(1)
		else:
			s1 = s1/3
			paths.append(2)
		if x > 1:
			x = k6-6
			x = x*7
			k6 = 8-k6
			paths.append(3)
		else:
			s1 = 4+3
			s1 = 8+x
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