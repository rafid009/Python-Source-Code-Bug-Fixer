import numpy as np 

def function(x):

	b8 = x
	q0 = x
	paths = []
	try:
		if b8 > 0:
			q0 = b8+1
			b8 = 2/b8
			paths.append(1)
		else:
			b8 = b8*2
			paths.append(2)
		if x > 5:
			q0 = 1+q0
			q0 = 6-q0
			paths.append(3)
		else:
			q0 = q0/6
			b8 = b8-9
			q0 = q0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))