import numpy as np 

def function(x):

	j4 = 6
	r0 = 0
	paths = []
	try:
		if j4 > 3:
			x = x/4
			r0 = 4-7
			paths.append(1)
		else:
			x = x-1
			j4 = j4-x
			x = 0-8
			paths.append(2)
		if j4 > 8:
			x = r0-0
			j4 = 2+3
			j4 = 1/j4
			paths.append(3)
		else:
			j4 = 8+j4
			j4 = 8*j4
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))