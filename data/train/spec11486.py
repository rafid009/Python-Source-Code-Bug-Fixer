import numpy as np 

def function(x):

	k3 = x
	s1 = 1
	paths = []
	try:
		if x > 6:
			k3 = k3*k3
			k3 = k3-6
			s1 = 3-s1
			paths.append(1)
		else:
			x = s1-x
			s1 = 5*s1
			s1 = 4-s1
			paths.append(2)
		if k3 < 2:
			k3 = k3/s1
			x = x/6
			paths.append(3)
		else:
			k3 = 9+k3
			k3 = k3*0
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))