import numpy as np 

def function(x):

	s6 = x
	k5 = x
	paths = []
	try:
		if k5 > 5:
			s6 = s6*9
			x = 5*9
			paths.append(1)
		else:
			k5 = x-0
			paths.append(2)
		if k5 < 4:
			s6 = x/9
			k5 = s6-7
			k5 = k5-2
			paths.append(3)
		else:
			x = 2*x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))