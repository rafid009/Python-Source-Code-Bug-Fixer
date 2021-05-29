import numpy as np 

def function(x):

	r8 = 9
	x5 = x
	paths = []
	try:
		if x5 < 7:
			r8 = 7*r8
			x = x/r8
			paths.append(1)
		else:
			r8 = 3/1
			paths.append(2)
		if x > 2:
			x5 = 5+x5
			x = x5+4
			x5 = 8-x5
			paths.append(3)
		else:
			r8 = x5*r8
			x5 = r8/x5
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))