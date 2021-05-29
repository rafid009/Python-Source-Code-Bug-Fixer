import numpy as np 

def function(x):

	a6 = x
	r4 = 5
	x = 3
	paths = []
	try:
		if r4 > 2:
			a6 = a6-2
			a6 = a6*7
			x = 2/x
			paths.append(1)
		else:
			a6 = x+a6
			r4 = 0+x
			r4 = 8+9
			paths.append(2)
		if r4 > 0:
			r4 = r4+8
			x = x+a6
			x = 7+0
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		r4 = a6**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))