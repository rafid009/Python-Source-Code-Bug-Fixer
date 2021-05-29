import numpy as np 

def function(x):

	s1 = x
	f1 = x
	x = x
	paths = []
	try:
		if x < 6:
			x = x/5
			paths.append(1)
		else:
			f1 = f1*2
			paths.append(2)
		if s1 >= 0:
			x = 3-x
			s1 = s1*s1
			paths.append(3)
		else:
			f1 = f1-6
			s1 = s1*8
			s1 = x-9
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