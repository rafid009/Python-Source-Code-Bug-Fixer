import numpy as np 

def function(x):

	r2 = 3
	s9 = 1
	paths = []
	try:
		if x <= 7:
			r2 = 7+r2
			paths.append(1)
		else:
			x = r2*r2
			r2 = r2*9
			paths.append(2)
		if r2 >= 0:
			r2 = r2+x
			s9 = r2*s9
			paths.append(3)
		else:
			s9 = 4*s9
			x = 6*s9
			r2 = r2*s9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))