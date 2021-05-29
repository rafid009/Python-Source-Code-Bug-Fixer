import numpy as np 

def function(x):

	s0 = x
	r1 = x
	paths = []
	try:
		if s0 <= 8:
			x = 2-x
			r1 = r1/8
			paths.append(1)
		else:
			x = 5+x
			r1 = r1/7
			r1 = 1-4
			paths.append(2)
		if r1 > 6:
			r1 = r1+4
			r1 = r1*3
			r1 = 3/r1
			paths.append(3)
		else:
			r1 = r1-x
			s0 = s0+0
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))