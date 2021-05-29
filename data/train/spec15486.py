import numpy as np 

def function(x):

	f2 = x
	s1 = x
	paths = []
	try:
		if x <= 5:
			s1 = s1+f2
			x = 5/x
			f2 = 3-s1
			paths.append(1)
		else:
			f2 = f2+2
			s1 = x+f2
			paths.append(2)
		if f2 >= 6:
			x = 9+x
			paths.append(3)
		else:
			x = 7-x
			s1 = s1-6
			f2 = f2-0
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