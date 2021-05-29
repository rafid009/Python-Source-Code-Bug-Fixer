import numpy as np 

def function(x):

	b4 = 2
	r5 = 4
	paths = []
	try:
		if b4 > 5:
			r5 = r5/b4
			b4 = 2*b4
			paths.append(1)
		else:
			r5 = 8/r5
			b4 = r5*b4
			b4 = x+b4
			paths.append(2)
		if x > 7:
			b4 = b4*x
			b4 = 1-b4
			paths.append(3)
		else:
			r5 = r5-b4
			b4 = b4-1
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))