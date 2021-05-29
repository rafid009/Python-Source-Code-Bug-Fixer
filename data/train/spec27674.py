import numpy as np 

def function(x):

	s1 = x
	o3 = 7
	paths = []
	try:
		if s1 < 0:
			s1 = s1-5
			s1 = x/s1
			o3 = s1-4
			paths.append(1)
		else:
			s1 = s1-1
			paths.append(2)
		if s1 > 7:
			s1 = 7*s1
			o3 = o3+8
			paths.append(3)
		else:
			o3 = 2/o3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))