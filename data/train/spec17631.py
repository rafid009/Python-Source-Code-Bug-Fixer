import numpy as np 

def function(x):

	e3 = 7
	s5 = 8
	x = x
	paths = []
	try:
		if x > 3:
			e3 = e3+x
			paths.append(1)
		else:
			s5 = 5+1
			x = x+4
			s5 = e3/s5
			paths.append(2)
		if s5 <= 0:
			e3 = e3+8
			paths.append(3)
		else:
			s5 = 5+3
			e3 = 3-7
			s5 = s5*7
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