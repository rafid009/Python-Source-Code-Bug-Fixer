import numpy as np 

def function(x):

	r7 = 9
	x9 = x
	paths = []
	try:
		if x9 >= 5:
			r7 = x9-5
			r7 = 8*r7
			r7 = r7/5
			paths.append(1)
		else:
			x = x9*1
			r7 = r7*9
			x9 = x9+x9
			paths.append(2)
		if x9 > 2:
			x = x-1
			paths.append(3)
		else:
			x9 = 1*x9
			x9 = 4+x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))