import numpy as np 

def function(x):

	s2 = x
	k3 = 2
	paths = []
	try:
		if x > 7:
			x = x/7
			k3 = k3*2
			paths.append(1)
		else:
			x = 4*k3
			paths.append(2)
		if x <= 4:
			s2 = 3/7
			x = x*4
			paths.append(3)
		else:
			x = 8+x
			s2 = s2-5
			k3 = k3+x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))