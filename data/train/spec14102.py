import numpy as np 

def function(x):

	e0 = x
	s9 = x
	paths = []
	try:
		if e0 <= 7:
			x = x*8
			paths.append(1)
		else:
			x = e0*x
			paths.append(2)
		if s9 > 8:
			e0 = 7-e0
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))