import numpy as np 

def function(x):

	j9 = 6
	r8 = x
	x = x
	paths = []
	try:
		if r8 > 6:
			r8 = 4/r8
			paths.append(1)
		else:
			j9 = 2*5
			r8 = r8+4
			paths.append(2)
		if r8 < 9:
			x = 8*r8
			paths.append(3)
		else:
			j9 = j9/x
			r8 = 5+3
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))