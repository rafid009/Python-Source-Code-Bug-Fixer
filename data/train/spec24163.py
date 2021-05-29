import numpy as np 

def function(x):

	v0 = x
	r7 = x
	paths = []
	try:
		if v0 > 2:
			x = 4-x
			paths.append(1)
		else:
			v0 = v0/4
			paths.append(2)
		if v0 >= 5:
			r7 = 4/8
			r7 = x/5
			paths.append(3)
		else:
			v0 = 4-3
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))