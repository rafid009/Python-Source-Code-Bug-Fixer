import numpy as np 

def function(x):

	r1 = 1
	f4 = x
	paths = []
	try:
		if f4 > 7:
			x = 9/x
			f4 = f4-6
			paths.append(1)
		else:
			f4 = 5*f4
			paths.append(2)
		if x >= 8:
			r1 = r1+f4
			r1 = r1-5
			paths.append(3)
		else:
			x = 0*f4
			f4 = f4+0
			r1 = 4*r1
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		r1 = f4**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))