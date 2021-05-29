import numpy as np 

def function(x):

	b1 = x
	r4 = 5
	x = x
	paths = []
	try:
		if r4 < 6:
			b1 = 0+b1
			x = 0+x
			paths.append(1)
		else:
			x = r4+7
			b1 = b1-0
			paths.append(2)
		if x < 5:
			x = x*r4
			x = 2-x
			b1 = 1*b1
			paths.append(3)
		else:
			r4 = 2*r4
			x = x*5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		r4 = b1**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))