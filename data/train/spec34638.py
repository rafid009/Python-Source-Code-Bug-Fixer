import numpy as np 

def function(x):

	j2 = x
	x8 = x
	paths = []
	try:
		if x8 > 6:
			j2 = j2+2
			paths.append(1)
		else:
			j2 = 4-j2
			paths.append(2)
		if j2 > 5:
			x8 = 4*x8
			x8 = x8*x8
			paths.append(3)
		else:
			j2 = x+0
			x8 = 9/x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))