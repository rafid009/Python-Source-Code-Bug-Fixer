import numpy as np 

def function(x):

	r2 = 7
	r6 = x
	paths = []
	try:
		if r6 >= 8:
			r6 = 1*r6
			r6 = 4*6
			r2 = 1/r2
			paths.append(1)
		else:
			x = 4*x
			x = x*x
			paths.append(2)
		if x < 3:
			r6 = 0+x
			x = 9-x
			r2 = 6-7
			paths.append(3)
		else:
			r6 = 3/r6
			x = r6*2
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r2 = r6**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))