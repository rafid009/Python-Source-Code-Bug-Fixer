import numpy as np 

def function(x):

	r5 = x
	b8 = 9
	paths = []
	try:
		if r5 > 8:
			b8 = r5/8
			paths.append(1)
		else:
			b8 = 4-6
			b8 = r5/b8
			paths.append(2)
		if b8 > 9:
			r5 = x+r5
			x = 2-x
			r5 = r5*x
			paths.append(3)
		else:
			r5 = r5-7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		r5 = b8**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))