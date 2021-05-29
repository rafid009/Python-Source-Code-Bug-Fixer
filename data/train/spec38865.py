import numpy as np 

def function(x):

	b8 = 6
	q3 = x
	paths = []
	try:
		if b8 <= 1:
			q3 = 4-q3
			q3 = 7*2
			paths.append(1)
		else:
			b8 = q3-x
			b8 = 0*b8
			paths.append(2)
		if b8 < 0:
			b8 = x+x
			x = 5/x
			q3 = x-x
			paths.append(3)
		else:
			b8 = q3-b8
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))