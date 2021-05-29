import numpy as np 

def function(x):

	s6 = 3
	q0 = x
	paths = []
	try:
		if s6 <= 5:
			s6 = s6-q0
			x = x*0
			paths.append(1)
		else:
			x = x+q0
			x = x/2
			s6 = 7/1
			paths.append(2)
		if s6 >= 3:
			q0 = q0/6
			x = 2+4
			paths.append(3)
		else:
			s6 = x*q0
			x = x-0
			q0 = 0/q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))