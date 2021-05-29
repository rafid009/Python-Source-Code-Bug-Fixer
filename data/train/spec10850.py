import numpy as np 

def function(x):

	s8 = 5
	f1 = x
	paths = []
	try:
		if x < 9:
			f1 = f1*9
			x = f1+x
			paths.append(1)
		else:
			x = 5+x
			x = 4-0
			paths.append(2)
		if f1 > 3:
			s8 = 1/s8
			f1 = 4/9
			f1 = 1+f1
			paths.append(3)
		else:
			f1 = f1+x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		s8 = f1**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))