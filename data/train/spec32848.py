import numpy as np 

def function(x):

	q9 = x
	r9 = 9
	paths = []
	try:
		if r9 < 8:
			x = x*9
			r9 = r9-5
			paths.append(1)
		else:
			r9 = 1-7
			paths.append(2)
		if x < 0:
			x = 4*9
			paths.append(3)
		else:
			r9 = r9/9
			r9 = 1/2
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		r9 = q9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))