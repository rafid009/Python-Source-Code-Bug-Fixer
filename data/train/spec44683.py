import numpy as np 

def function(x):

	k6 = x
	f1 = 2
	paths = []
	try:
		if k6 < 0:
			k6 = 5+6
			k6 = 0*k6
			paths.append(1)
		else:
			f1 = f1/k6
			k6 = 2+f1
			paths.append(2)
		if k6 <= 8:
			x = x-8
			f1 = 7/f1
			k6 = k6*6
			paths.append(3)
		else:
			k6 = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))