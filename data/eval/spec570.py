import numpy as np 

def function(x):

	e9 = 5
	s9 = 2
	paths = []
	try:
		if e9 >= 6:
			x = x*0
			e9 = s9+e9
			paths.append(1)
		else:
			e9 = x+4
			s9 = 4+s9
			s9 = x+7
			paths.append(2)
		if s9 < 7:
			x = x*6
			paths.append(3)
		else:
			x = 3-8
			s9 = s9-1
			e9 = 7/e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		s9 = e9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))