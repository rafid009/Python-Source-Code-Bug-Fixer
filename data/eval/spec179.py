import numpy as np 

def function(x):

	r5 = x
	b2 = x
	paths = []
	try:
		if r5 > 9:
			r5 = 5-0
			r5 = 5+r5
			b2 = r5-1
			paths.append(1)
		else:
			r5 = r5*1
			x = x+b2
			paths.append(2)
		if r5 >= 9:
			x = 3*x
			x = b2*r5
			paths.append(3)
		else:
			r5 = 1/b2
			b2 = b2*1
			r5 = 7-r5
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))