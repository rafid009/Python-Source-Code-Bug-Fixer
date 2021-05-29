import numpy as np 

def function(x):

	r5 = x
	l0 = x
	paths = []
	try:
		if l0 >= 4:
			x = 0*7
			r5 = 7-4
			r5 = 7/r5
			paths.append(1)
		else:
			x = 3*x
			l0 = 4*l0
			paths.append(2)
		if x < 8:
			x = 0-r5
			paths.append(3)
		else:
			l0 = 0+1
			r5 = r5*9
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		l0 = r5**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))