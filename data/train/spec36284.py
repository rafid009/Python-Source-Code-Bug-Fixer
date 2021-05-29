import numpy as np 

def function(x):

	e9 = 4
	s2 = x
	paths = []
	try:
		if x > 7:
			e9 = 0+s2
			e9 = e9+9
			paths.append(1)
		else:
			e9 = e9+4
			paths.append(2)
		if e9 < 3:
			s2 = x*s2
			s2 = s2-5
			paths.append(3)
		else:
			x = s2*s2
			e9 = s2/e9
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		e9 = s2**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))