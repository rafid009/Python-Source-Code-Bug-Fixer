import numpy as np 

def function(x):

	r8 = x
	r2 = 0
	paths = []
	try:
		if r2 < 5:
			r8 = r8/3
			x = x-1
			paths.append(1)
		else:
			x = 1-x
			r8 = 3*r8
			paths.append(2)
		if x <= 6:
			r2 = 4-r2
			paths.append(3)
		else:
			r2 = 1*r2
			r2 = r2/2
			r2 = r2-5
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r8 = r2**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))