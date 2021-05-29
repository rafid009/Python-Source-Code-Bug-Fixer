import numpy as np 

def function(x):

	b6 = 6
	r0 = x
	paths = []
	try:
		if b6 < 8:
			x = b6*x
			b6 = x*6
			r0 = r0+4
			paths.append(1)
		else:
			x = x+x
			b6 = b6/3
			b6 = 7/b6
			paths.append(2)
		if b6 > 5:
			x = 4-7
			r0 = 7+0
			paths.append(3)
		else:
			b6 = 1/6
			x = 5*x
			b6 = x-2
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		r0 = b6**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))