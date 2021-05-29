import numpy as np 

def function(x):

	f1 = x
	r0 = x
	paths = []
	try:
		if f1 > 7:
			r0 = 1*7
			r0 = 5-x
			f1 = f1-7
			paths.append(1)
		else:
			x = x-0
			r0 = r0/3
			r0 = 2/r0
			paths.append(2)
		if r0 >= 3:
			x = x-4
			paths.append(3)
		else:
			r0 = 2/7
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))