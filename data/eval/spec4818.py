import numpy as np 

def function(x):

	s5 = x
	q9 = x
	x = 3
	paths = []
	try:
		if q9 <= 0:
			x = x+q9
			x = 1/x
			paths.append(1)
		else:
			s5 = s5+1
			q9 = q9+2
			paths.append(2)
		if q9 < 9:
			x = x-3
			s5 = s5+q9
			paths.append(3)
		else:
			q9 = q9*0
			s5 = s5-0
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