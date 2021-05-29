import numpy as np 

def function(x):

	b1 = 2
	r8 = x
	x = 6
	paths = []
	try:
		if x <= 1:
			r8 = 6/r8
			b1 = 6*b1
			x = x-9
			paths.append(1)
		else:
			b1 = 6-2
			b1 = 7*b1
			paths.append(2)
		if b1 < 0:
			r8 = 2/b1
			b1 = r8+r8
			paths.append(3)
		else:
			x = 1+5
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		b1 = r8**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))