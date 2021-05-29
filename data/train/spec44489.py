import numpy as np 

def function(x):

	v0 = x
	q4 = 8
	paths = []
	try:
		if v0 <= 1:
			v0 = v0*8
			paths.append(1)
		else:
			q4 = q4-1
			q4 = q4/q4
			q4 = q4-v0
			paths.append(2)
		if x < 6:
			x = x+1
			paths.append(3)
		else:
			q4 = 6+q4
			x = 8-7
			q4 = q4/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))