import numpy as np 

def function(x):

	r4 = 1
	a1 = x
	paths = []
	try:
		if x < 9:
			r4 = r4*x
			paths.append(1)
		else:
			a1 = x*7
			x = 6/5
			paths.append(2)
		if a1 <= 8:
			a1 = 0*r4
			paths.append(3)
		else:
			a1 = a1/9
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		a1 = r4**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))