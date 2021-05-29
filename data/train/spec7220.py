import numpy as np 

def function(x):

	r1 = x
	l0 = 7
	paths = []
	try:
		if x >= 5:
			r1 = r1/2
			r1 = r1+6
			r1 = r1*7
			paths.append(1)
		else:
			r1 = r1-9
			r1 = r1-8
			paths.append(2)
		if l0 > 2:
			l0 = l0*8
			x = 5-x
			paths.append(3)
		else:
			x = x-2
			r1 = r1/1
			l0 = 0*x
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))