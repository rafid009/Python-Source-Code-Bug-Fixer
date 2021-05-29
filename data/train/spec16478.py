import numpy as np 

def function(x):

	k9 = 8
	s1 = x
	paths = []
	try:
		if k9 < 9:
			k9 = 4*s1
			k9 = x-k9
			k9 = k9-5
			paths.append(1)
		else:
			k9 = k9*1
			s1 = s1*4
			paths.append(2)
		if k9 >= 2:
			s1 = k9*5
			s1 = x+s1
			k9 = 4-5
			paths.append(3)
		else:
			x = x*k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		s1 = k9**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))