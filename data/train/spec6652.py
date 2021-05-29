import numpy as np 

def function(x):

	s5 = 0
	f3 = x
	paths = []
	try:
		if f3 >= 5:
			s5 = 5*1
			x = x/4
			paths.append(1)
		else:
			x = 7-6
			s5 = f3+s5
			f3 = f3+0
			paths.append(2)
		if s5 < 1:
			x = f3-x
			paths.append(3)
		else:
			x = 3+x
			x = 7/f3
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))