import numpy as np 

def function(x):

	r9 = 8
	v0 = 8
	paths = []
	try:
		if v0 > 7:
			v0 = v0+7
			paths.append(1)
		else:
			v0 = v0-v0
			v0 = r9+x
			v0 = r9*5
			paths.append(2)
		if v0 > 3:
			r9 = r9/x
			v0 = v0-8
			paths.append(3)
		else:
			v0 = 6*v0
			x = 7+x
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		v0 = r9**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))