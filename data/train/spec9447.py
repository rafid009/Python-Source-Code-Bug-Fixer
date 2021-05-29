import numpy as np 

def function(x):

	s2 = 4
	r3 = 4
	paths = []
	try:
		if r3 > 7:
			r3 = 2*r3
			x = s2+x
			x = s2*x
			paths.append(1)
		else:
			s2 = s2*4
			s2 = 4-8
			s2 = x+s2
			paths.append(2)
		if s2 >= 4:
			x = x-6
			x = x-2
			paths.append(3)
		else:
			r3 = r3*s2
			r3 = 4+s2
			s2 = x*s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))