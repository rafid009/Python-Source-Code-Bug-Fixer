import numpy as np 

def function(x):

	f5 = 2
	u2 = x
	paths = []
	try:
		if x > 9:
			x = 8/x
			paths.append(1)
		else:
			x = u2+7
			f5 = 2*6
			paths.append(2)
		if u2 > 8:
			x = x-7
			paths.append(3)
		else:
			x = 5+2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		f5 = u2**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))