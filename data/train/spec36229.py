import numpy as np 

def function(x):

	a4 = x
	s9 = 3
	paths = []
	try:
		if x <= 6:
			s9 = s9/x
			s9 = 1-x
			paths.append(1)
		else:
			a4 = 8/6
			a4 = a4+s9
			paths.append(2)
		if a4 < 8:
			x = x+1
			paths.append(3)
		else:
			a4 = a4/4
			x = s9+7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))