import numpy as np 

def function(x):

	s4 = 6
	q4 = x
	paths = []
	try:
		if x < 0:
			q4 = q4-4
			x = x-6
			paths.append(1)
		else:
			s4 = 3*x
			x = 2*x
			s4 = s4/8
			paths.append(2)
		if s4 > 5:
			x = x/4
			s4 = 6+s4
			x = q4*x
			paths.append(3)
		else:
			x = s4-0
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))