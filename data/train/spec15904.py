import numpy as np 

def function(x):

	b7 = x
	r5 = 2
	paths = []
	try:
		if b7 < 3:
			b7 = b7+x
			paths.append(1)
		else:
			b7 = b7*5
			paths.append(2)
		if r5 >= 9:
			x = 6-x
			x = r5+x
			r5 = r5*r5
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))