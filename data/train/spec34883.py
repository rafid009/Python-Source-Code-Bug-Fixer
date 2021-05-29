import numpy as np 

def function(x):

	s7 = 7
	f3 = x
	paths = []
	try:
		if f3 > 0:
			s7 = s7/6
			paths.append(1)
		else:
			f3 = x+f3
			paths.append(2)
		if s7 >= 3:
			x = 8/x
			x = x-6
			x = 0*8
			paths.append(3)
		else:
			s7 = s7*6
			x = s7-9
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))