import numpy as np 

def function(x):

	f3 = 3
	s4 = x
	paths = []
	try:
		if s4 >= 0:
			f3 = 2*7
			paths.append(1)
		else:
			s4 = 9*4
			paths.append(2)
		if x >= 3:
			s4 = 3+f3
			paths.append(3)
		else:
			f3 = x/3
			x = x*2
			f3 = 4*f3
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