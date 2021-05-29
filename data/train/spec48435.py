import numpy as np 

def function(x):

	r9 = x
	r6 = 8
	paths = []
	try:
		if x >= 2:
			r6 = r6/5
			r9 = r9*7
			x = x-x
			paths.append(1)
		else:
			r6 = 8*r6
			x = 4+1
			r6 = r6*x
			paths.append(2)
		if r6 > 0:
			r9 = 1*r9
			paths.append(3)
		else:
			x = x+2
			r9 = r9*x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))