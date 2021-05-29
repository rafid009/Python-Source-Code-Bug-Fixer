import numpy as np 

def function(x):

	s5 = 4
	f1 = 1
	paths = []
	try:
		if x >= 3:
			x = 0+x
			paths.append(1)
		else:
			s5 = 9/s5
			s5 = s5-x
			x = f1-x
			paths.append(2)
		if x > 4:
			f1 = 9+8
			paths.append(3)
		else:
			f1 = f1/s5
			s5 = s5/s5
			s5 = 2+7
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		s5 = f1**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))