import numpy as np 

def function(x):

	r8 = x
	b5 = 1
	paths = []
	try:
		if r8 > 7:
			x = 3/r8
			b5 = 1*x
			r8 = 8-9
			paths.append(1)
		else:
			b5 = 6*1
			b5 = x-b5
			r8 = 8-r8
			paths.append(2)
		if r8 <= 5:
			b5 = b5/8
			b5 = b5/7
			x = 4+x
			paths.append(3)
		else:
			x = 1-7
			b5 = 0-b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		r8 = b5**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))