import numpy as np 

def function(x):

	b6 = x
	x8 = 2
	paths = []
	try:
		if b6 > 5:
			x = 5*6
			x8 = x8-x
			x8 = 2+x8
			paths.append(1)
		else:
			b6 = 8/b6
			b6 = 2-b6
			paths.append(2)
		if b6 <= 9:
			x8 = x8-x8
			x8 = 0/9
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x8 = b6**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))