import numpy as np 

def function(x):

	e5 = 6
	s8 = 5
	paths = []
	try:
		if x > 9:
			s8 = 1*x
			x = 2-x
			paths.append(1)
		else:
			e5 = 9+x
			paths.append(2)
		if e5 <= 9:
			s8 = e5/s8
			x = 4*0
			paths.append(3)
		else:
			e5 = e5/2
			x = s8+e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))