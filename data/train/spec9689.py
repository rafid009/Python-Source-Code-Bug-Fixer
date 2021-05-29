import numpy as np 

def function(x):

	x8 = 3
	v7 = x
	paths = []
	try:
		if x8 < 0:
			x8 = 1-8
			v7 = v7*2
			x = x*8
			paths.append(1)
		else:
			x8 = x8*9
			x = 3+x8
			x8 = x8-6
			paths.append(2)
		if x > 5:
			x = x8+x
			x = 7+x
			paths.append(3)
		else:
			x = 8/x8
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x8 = v7**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))