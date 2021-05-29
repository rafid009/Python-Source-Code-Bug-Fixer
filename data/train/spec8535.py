import numpy as np 

def function(x):

	k1 = x
	r4 = x
	paths = []
	try:
		if r4 < 8:
			r4 = 3-x
			x = 7/x
			paths.append(1)
		else:
			r4 = 5+5
			r4 = r4+7
			r4 = r4/6
			paths.append(2)
		if k1 < 9:
			r4 = 6*3
			k1 = 8+k1
			paths.append(3)
		else:
			x = r4-r4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		r4 = k1**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))