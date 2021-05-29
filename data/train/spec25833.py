import numpy as np 

def function(x):

	f5 = x
	s4 = 9
	x = 1
	paths = []
	try:
		if s4 > 0:
			x = 8/f5
			paths.append(1)
		else:
			x = s4+f5
			paths.append(2)
		if x >= 5:
			f5 = f5*s4
			f5 = s4*f5
			paths.append(3)
		else:
			s4 = s4/x
			x = 0+7
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))