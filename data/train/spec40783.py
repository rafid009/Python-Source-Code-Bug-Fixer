import numpy as np 

def function(x):

	s9 = x
	e2 = x
	paths = []
	try:
		if e2 > 8:
			e2 = e2+5
			x = x+5
			paths.append(1)
		else:
			x = x*x
			e2 = e2+7
			e2 = 1-e2
			paths.append(2)
		if s9 < 0:
			x = x+9
			paths.append(3)
		else:
			s9 = s9-x
			e2 = x/3
			s9 = 0/s9
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))