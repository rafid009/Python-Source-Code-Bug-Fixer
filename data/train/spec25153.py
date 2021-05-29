import numpy as np 

def function(x):

	l0 = x
	r9 = 5
	paths = []
	try:
		if l0 < 2:
			r9 = 4+x
			paths.append(1)
		else:
			r9 = 8/r9
			r9 = r9*r9
			paths.append(2)
		if r9 > 3:
			r9 = l0*3
			r9 = r9-3
			paths.append(3)
		else:
			l0 = l0/4
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		l0 = r9**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))