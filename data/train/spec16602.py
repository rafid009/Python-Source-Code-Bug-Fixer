import numpy as np 

def function(x):

	r7 = 5
	l4 = 2
	x = x
	paths = []
	try:
		if r7 > 8:
			r7 = 5*8
			r7 = r7+2
			r7 = l4/8
			paths.append(1)
		else:
			r7 = r7+x
			paths.append(2)
		if r7 <= 5:
			r7 = 7*r7
			r7 = 7/6
			l4 = r7+l4
			paths.append(3)
		else:
			r7 = 4-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))