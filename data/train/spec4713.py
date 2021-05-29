import numpy as np 

def function(x):

	s9 = x
	q0 = 6
	paths = []
	try:
		if q0 <= 2:
			s9 = s9+q0
			paths.append(1)
		else:
			s9 = 8/5
			paths.append(2)
		if x < 6:
			q0 = s9-q0
			s9 = s9+9
			x = x*1
			paths.append(3)
		else:
			s9 = 4*3
			q0 = 2*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))