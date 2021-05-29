import numpy as np 

def function(x):

	v9 = 4
	r9 = 6
	paths = []
	try:
		if v9 > 1:
			r9 = 5*x
			paths.append(1)
		else:
			r9 = v9+0
			r9 = 7+0
			paths.append(2)
		if x <= 6:
			x = v9+3
			paths.append(3)
		else:
			r9 = 0+9
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