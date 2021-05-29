import numpy as np 

def function(x):

	f6 = 1
	r1 = 9
	paths = []
	try:
		if r1 >= 9:
			r1 = r1-6
			paths.append(1)
		else:
			x = x-7
			f6 = f6-2
			paths.append(2)
		if r1 >= 7:
			f6 = 4*f6
			paths.append(3)
		else:
			f6 = f6*4
			x = 3/6
			f6 = 3-4
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		r1 = f6**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))