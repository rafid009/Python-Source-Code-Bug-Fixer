import numpy as np 

def function(x):

	r3 = x
	b8 = x
	x = 5
	paths = []
	try:
		if b8 < 3:
			b8 = 3*b8
			x = r3/x
			x = 1*x
			paths.append(1)
		else:
			x = b8+x
			x = x*7
			b8 = b8*6
			paths.append(2)
		if r3 > 9:
			x = b8+r3
			r3 = r3+6
			paths.append(3)
		else:
			r3 = 8-x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		r3 = b8**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))