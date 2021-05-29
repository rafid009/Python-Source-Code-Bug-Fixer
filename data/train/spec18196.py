import numpy as np 

def function(x):

	s4 = x
	r5 = 8
	paths = []
	try:
		if s4 > 1:
			x = 6-s4
			s4 = s4/x
			s4 = s4*0
			paths.append(1)
		else:
			r5 = 5/1
			x = 8-x
			s4 = s4-2
			paths.append(2)
		if s4 <= 7:
			x = x*1
			r5 = r5/7
			paths.append(3)
		else:
			s4 = x-5
			r5 = s4+3
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))