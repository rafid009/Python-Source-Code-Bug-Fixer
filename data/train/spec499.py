import numpy as np 

def function(x):

	q4 = 0
	s4 = x
	paths = []
	try:
		if q4 >= 2:
			s4 = s4+6
			x = x-s4
			paths.append(1)
		else:
			q4 = q4+s4
			x = x*0
			paths.append(2)
		if s4 <= 9:
			q4 = q4-7
			s4 = q4/5
			paths.append(3)
		else:
			s4 = 2-q4
			s4 = 2*s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		q4 = s4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))