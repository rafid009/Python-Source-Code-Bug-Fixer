import numpy as np 

def function(x):

	q2 = x
	b8 = 7
	paths = []
	try:
		if q2 < 6:
			q2 = q2-0
			paths.append(1)
		else:
			b8 = x-6
			b8 = 6+x
			x = x-x
			paths.append(2)
		if x > 2:
			b8 = 8/3
			q2 = q2*2
			q2 = 0+q2
			paths.append(3)
		else:
			b8 = b8-7
			b8 = x-b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))