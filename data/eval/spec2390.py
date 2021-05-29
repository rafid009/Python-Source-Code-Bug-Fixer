import numpy as np 

def function(x):

	r6 = 6
	f1 = 8
	paths = []
	try:
		if r6 <= 9:
			r6 = r6*7
			x = 3-5
			r6 = 3*9
			paths.append(1)
		else:
			f1 = r6*f1
			paths.append(2)
		if f1 > 6:
			r6 = 1-r6
			f1 = 4-f1
			r6 = r6-5
			paths.append(3)
		else:
			f1 = f1+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))