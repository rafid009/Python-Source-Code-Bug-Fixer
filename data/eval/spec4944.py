import numpy as np 

def function(x):

	r4 = 2
	v1 = x
	paths = []
	try:
		if r4 <= 6:
			x = 0-x
			v1 = 2*v1
			paths.append(1)
		else:
			r4 = r4-1
			r4 = 8/8
			v1 = 9+1
			paths.append(2)
		if v1 < 9:
			r4 = r4/3
			r4 = 0/r4
			paths.append(3)
		else:
			v1 = 7*v1
			x = x-1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))