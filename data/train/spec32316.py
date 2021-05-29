import numpy as np 

def function(x):

	k5 = x
	r4 = 5
	paths = []
	try:
		if x < 0:
			k5 = 2/k5
			paths.append(1)
		else:
			k5 = r4+x
			r4 = r4+1
			paths.append(2)
		if x >= 8:
			r4 = k5+k5
			paths.append(3)
		else:
			r4 = r4-9
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))