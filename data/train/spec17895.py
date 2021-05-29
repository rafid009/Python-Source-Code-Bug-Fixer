import numpy as np 

def function(x):

	b6 = 9
	r5 = x
	paths = []
	try:
		if x <= 2:
			b6 = r5+b6
			paths.append(1)
		else:
			r5 = 3-x
			r5 = r5*5
			r5 = x/r5
			paths.append(2)
		if b6 < 4:
			r5 = r5/8
			b6 = b6+b6
			r5 = r5/8
			paths.append(3)
		else:
			x = x-2
			b6 = 3-b6
			b6 = 6-3
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		r5 = b6**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))