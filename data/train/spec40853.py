import numpy as np 

def function(x):

	r3 = 6
	i4 = x
	paths = []
	try:
		if r3 < 9:
			r3 = 7-8
			paths.append(1)
		else:
			r3 = 5+r3
			r3 = 9/r3
			r3 = r3+7
			paths.append(2)
		if i4 < 9:
			r3 = r3/8
			paths.append(3)
		else:
			i4 = i4+5
			x = x/4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		r3 = i4**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))