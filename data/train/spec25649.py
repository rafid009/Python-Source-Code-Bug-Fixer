import numpy as np 

def function(x):

	b6 = x
	q3 = 0
	x = 2
	paths = []
	try:
		if q3 <= 5:
			q3 = 0+q3
			q3 = q3/2
			paths.append(1)
		else:
			q3 = b6-q3
			x = 7+8
			paths.append(2)
		if q3 < 7:
			b6 = x+b6
			q3 = 5-3
			q3 = q3/b6
			paths.append(3)
		else:
			x = b6-x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))