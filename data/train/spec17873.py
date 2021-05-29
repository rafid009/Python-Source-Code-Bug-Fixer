import numpy as np 

def function(x):

	q0 = x
	v8 = x
	paths = []
	try:
		if x < 4:
			v8 = 3-v8
			paths.append(1)
		else:
			x = 1/x
			q0 = q0*8
			q0 = q0*q0
			paths.append(2)
		if x <= 4:
			x = x-8
			q0 = x-1
			v8 = q0/v8
			paths.append(3)
		else:
			x = x+4
			q0 = x+x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))