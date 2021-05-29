import numpy as np 

def function(x):

	e3 = 7
	s2 = x
	paths = []
	try:
		if x < 6:
			e3 = e3*s2
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if e3 > 8:
			s2 = 9/s2
			s2 = x/9
			s2 = e3/s2
			paths.append(3)
		else:
			x = 7+8
			s2 = s2+e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))