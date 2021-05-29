import numpy as np 

def function(x):

	f2 = x
	s9 = 6
	paths = []
	try:
		if x > 1:
			s9 = s9/9
			s9 = s9+f2
			paths.append(1)
		else:
			f2 = f2-2
			x = 3/x
			f2 = 2*f2
			paths.append(2)
		if x < 0:
			s9 = 7*s9
			paths.append(3)
		else:
			s9 = s9-x
			f2 = 5+f2
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		f2 = s9**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))