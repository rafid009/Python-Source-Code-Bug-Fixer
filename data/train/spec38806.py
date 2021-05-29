import numpy as np 

def function(x):

	r8 = x
	x5 = x
	paths = []
	try:
		if x5 >= 4:
			x = x/r8
			paths.append(1)
		else:
			x5 = 6-x5
			x = x/1
			r8 = 8/r8
			paths.append(2)
		if r8 <= 5:
			x5 = x-5
			r8 = 7/r8
			paths.append(3)
		else:
			r8 = 4+r8
			x5 = 9+6
			x5 = 4-2
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x5 = r8**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))