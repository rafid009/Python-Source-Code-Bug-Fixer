import numpy as np 

def function(x):

	b5 = x
	r7 = x
	paths = []
	try:
		if b5 > 9:
			x = 3+x
			paths.append(1)
		else:
			r7 = 5-8
			paths.append(2)
		if x >= 0:
			r7 = 8-1
			paths.append(3)
		else:
			x = 3-0
			r7 = 0+r7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		r7 = b5**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))