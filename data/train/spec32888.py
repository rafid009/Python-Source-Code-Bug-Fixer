import numpy as np 

def function(x):

	z7 = 5
	r8 = x
	x = 7
	paths = []
	try:
		if x > 4:
			r8 = 3/r8
			paths.append(1)
		else:
			r8 = 8/1
			z7 = z7*z7
			paths.append(2)
		if x < 1:
			r8 = 1-x
			x = 6-4
			paths.append(3)
		else:
			r8 = z7-r8
			x = z7/z7
			r8 = 6+r8
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