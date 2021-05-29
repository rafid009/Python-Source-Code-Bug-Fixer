import numpy as np 

def function(x):

	s1 = 8
	d9 = x
	paths = []
	try:
		if d9 >= 1:
			d9 = 5*x
			d9 = d9*2
			paths.append(1)
		else:
			s1 = 0+8
			s1 = 2*5
			x = 2-x
			paths.append(2)
		if s1 > 2:
			d9 = d9-x
			d9 = x-s1
			s1 = x/s1
			paths.append(3)
		else:
			x = 0*5
			s1 = s1+d9
			d9 = d9*d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))