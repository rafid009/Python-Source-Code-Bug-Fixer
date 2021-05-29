import numpy as np 

def function(x):

	e2 = x
	s4 = x
	paths = []
	try:
		if x > 9:
			s4 = s4/6
			x = x+e2
			s4 = 3/s4
			paths.append(1)
		else:
			e2 = e2+1
			e2 = 3-9
			paths.append(2)
		if s4 > 5:
			x = 7+e2
			paths.append(3)
		else:
			e2 = 7+3
			x = s4/1
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