import numpy as np 

def function(x):

	k2 = x
	f6 = x
	paths = []
	try:
		if f6 < 8:
			x = k2-x
			paths.append(1)
		else:
			x = x+x
			k2 = 5-k2
			paths.append(2)
		if x > 0:
			k2 = 1*f6
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		f6 = k2**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))