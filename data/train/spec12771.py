import numpy as np 

def function(x):

	r2 = x
	l6 = 2
	paths = []
	try:
		if x <= 4:
			r2 = r2-9
			l6 = 2*7
			paths.append(1)
		else:
			l6 = 6-x
			x = 0*x
			paths.append(2)
		if r2 >= 3:
			l6 = 5+l6
			x = r2*1
			x = 4-x
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))