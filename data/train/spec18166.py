import numpy as np 

def function(x):

	a4 = x
	r9 = x
	paths = []
	try:
		if a4 >= 0:
			r9 = r9/r9
			paths.append(1)
		else:
			a4 = a4+8
			x = 7*x
			a4 = 0-1
			paths.append(2)
		if x > 4:
			r9 = r9/a4
			paths.append(3)
		else:
			x = x+9
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		a4 = r9**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))