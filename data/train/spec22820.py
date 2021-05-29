import numpy as np 

def function(x):

	s1 = 2
	f5 = 2
	paths = []
	try:
		if f5 <= 3:
			s1 = s1*1
			f5 = f5+f5
			f5 = x*f5
			paths.append(1)
		else:
			f5 = f5/2
			s1 = 9+s1
			f5 = f5+8
			paths.append(2)
		if x <= 9:
			f5 = f5-0
			x = 4-x
			f5 = f5/5
			paths.append(3)
		else:
			f5 = 8/f5
			f5 = x/2
			s1 = s1-s1
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		s1 = f5**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))