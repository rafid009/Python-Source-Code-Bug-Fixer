import numpy as np 

def function(x):

	r2 = x
	f7 = 1
	paths = []
	try:
		if f7 >= 1:
			r2 = r2+r2
			paths.append(1)
		else:
			f7 = r2/f7
			f7 = r2*3
			f7 = x*6
			paths.append(2)
		if f7 < 5:
			f7 = r2/f7
			f7 = f7-6
			paths.append(3)
		else:
			x = x/6
			f7 = f7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))