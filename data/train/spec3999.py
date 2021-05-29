import numpy as np 

def function(x):

	x2 = x
	f5 = 1
	paths = []
	try:
		if x2 >= 7:
			x = f5*x2
			f5 = f5-f5
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if x2 > 5:
			f5 = f5-4
			x2 = f5*5
			x2 = x2+0
			paths.append(3)
		else:
			x2 = x2*2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))