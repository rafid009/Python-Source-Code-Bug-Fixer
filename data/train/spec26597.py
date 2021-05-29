import numpy as np 

def function(x):

	b1 = x
	v6 = 0
	x = x
	paths = []
	try:
		if b1 >= 2:
			b1 = v6*x
			b1 = b1-2
			x = 1+b1
			paths.append(1)
		else:
			b1 = b1/9
			b1 = 3/1
			b1 = b1/8
			paths.append(2)
		if v6 > 1:
			x = 3*x
			b1 = b1-3
			paths.append(3)
		else:
			b1 = 1*b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		v6 = b1**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))