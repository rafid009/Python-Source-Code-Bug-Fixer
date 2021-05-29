import numpy as np 

def function(x):

	s7 = x
	f2 = 2
	paths = []
	try:
		if f2 >= 3:
			x = x*f2
			paths.append(1)
		else:
			f2 = f2/2
			f2 = f2/6
			x = x*f2
			paths.append(2)
		if x >= 3:
			s7 = s7*x
			paths.append(3)
		else:
			s7 = 1*0
			f2 = f2-9
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))