import numpy as np 

def function(x):

	j5 = x
	b6 = x
	paths = []
	try:
		if b6 <= 6:
			j5 = b6*j5
			x = 7-x
			paths.append(1)
		else:
			j5 = 6-j5
			j5 = 8*j5
			paths.append(2)
		if x > 0:
			j5 = j5+8
			paths.append(3)
		else:
			x = x/3
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