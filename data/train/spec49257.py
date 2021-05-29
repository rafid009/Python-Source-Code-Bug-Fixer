import numpy as np 

def function(x):

	r1 = x
	b1 = 6
	paths = []
	try:
		if r1 >= 4:
			x = 1+7
			b1 = 1/r1
			paths.append(1)
		else:
			x = x+x
			r1 = x-0
			x = 4*x
			paths.append(2)
		if r1 <= 8:
			b1 = b1/5
			b1 = 2/b1
			x = 3-x
			paths.append(3)
		else:
			x = r1/x
			b1 = b1-3
			b1 = b1-x
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		b1 = r1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))