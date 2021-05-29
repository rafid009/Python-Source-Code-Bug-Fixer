import numpy as np 

def function(x):

	a9 = x
	k6 = 8
	paths = []
	try:
		if a9 <= 0:
			a9 = a9-4
			a9 = 6-k6
			k6 = 3/9
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if a9 <= 5:
			k6 = a9-0
			paths.append(3)
		else:
			x = a9+x
			k6 = a9-9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))