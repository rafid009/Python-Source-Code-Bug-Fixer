import numpy as np 

def function(x):

	d2 = x
	s2 = 4
	paths = []
	try:
		if d2 > 2:
			d2 = d2+0
			s2 = 5*s2
			x = x*7
			paths.append(1)
		else:
			x = 6/x
			x = x-6
			s2 = x/s2
			paths.append(2)
		if d2 < 2:
			s2 = 4-x
			d2 = s2-d2
			paths.append(3)
		else:
			d2 = d2+8
			s2 = 3-0
			x = d2+x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		d2 = s2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))