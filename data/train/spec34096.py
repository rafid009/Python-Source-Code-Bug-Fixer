import numpy as np 

def function(x):

	a9 = x
	r3 = 1
	x = 7
	paths = []
	try:
		if x > 8:
			r3 = x/r3
			paths.append(1)
		else:
			a9 = a9-7
			a9 = 6*a9
			paths.append(2)
		if r3 >= 1:
			r3 = x+4
			r3 = r3+8
			x = 3*7
			paths.append(3)
		else:
			x = x*3
			r3 = r3+7
			x = x+4
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))