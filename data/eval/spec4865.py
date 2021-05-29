import numpy as np 

def function(x):

	r1 = x
	j9 = x
	x = 7
	paths = []
	try:
		if x >= 1:
			r1 = r1-0
			r1 = j9+6
			paths.append(1)
		else:
			x = x-r1
			j9 = j9-j9
			paths.append(2)
		if j9 <= 8:
			j9 = 9+r1
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))