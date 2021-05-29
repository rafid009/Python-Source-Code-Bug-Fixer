import numpy as np 

def function(x):

	k6 = 6
	f2 = x
	paths = []
	try:
		if k6 >= 2:
			k6 = 3*0
			paths.append(1)
		else:
			f2 = 1*3
			paths.append(2)
		if x <= 9:
			f2 = f2/2
			paths.append(3)
		else:
			k6 = 5-k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))