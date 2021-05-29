import numpy as np 

def function(x):

	r0 = x
	j5 = 5
	paths = []
	try:
		if j5 > 3:
			x = 0-x
			j5 = j5/j5
			paths.append(1)
		else:
			j5 = 9-j5
			j5 = 6*3
			r0 = 6/r0
			paths.append(2)
		if r0 <= 9:
			x = 8*x
			paths.append(3)
		else:
			x = x+x
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