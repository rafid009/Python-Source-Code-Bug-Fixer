import numpy as np 

def function(x):

	r7 = 8
	b7 = 9
	paths = []
	try:
		if b7 < 0:
			r7 = 3*r7
			r7 = b7/3
			b7 = 4*3
			paths.append(1)
		else:
			r7 = r7*1
			r7 = r7+5
			b7 = b7-1
			paths.append(2)
		if x < 7:
			r7 = b7/r7
			r7 = x/r7
			r7 = r7/2
			paths.append(3)
		else:
			x = b7*6
			r7 = 7-0
			x = x*x
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