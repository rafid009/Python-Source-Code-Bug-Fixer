import numpy as np 

def function(x):

	b8 = x
	r5 = x
	x = 1
	paths = []
	try:
		if r5 < 5:
			x = x-4
			x = r5-0
			x = x*5
			paths.append(1)
		else:
			x = 5*b8
			paths.append(2)
		if x > 6:
			r5 = x*r5
			b8 = b8*b8
			x = x+8
			paths.append(3)
		else:
			r5 = r5*r5
			r5 = x+r5
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))