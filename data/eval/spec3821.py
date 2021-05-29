import numpy as np 

def function(x):

	q4 = x
	r8 = 9
	paths = []
	try:
		if q4 <= 1:
			r8 = r8*1
			paths.append(1)
		else:
			r8 = r8-9
			paths.append(2)
		if r8 <= 6:
			q4 = r8*9
			q4 = 1+4
			paths.append(3)
		else:
			r8 = r8/3
			q4 = 8+q4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))