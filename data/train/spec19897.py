import numpy as np 

def function(x):

	s1 = x
	k1 = x
	x = 5
	paths = []
	try:
		if k1 < 9:
			x = 1/x
			k1 = s1/k1
			paths.append(1)
		else:
			k1 = k1*0
			paths.append(2)
		if s1 < 5:
			k1 = s1+x
			paths.append(3)
		else:
			k1 = k1/s1
			s1 = s1*9
			k1 = 5+6
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))