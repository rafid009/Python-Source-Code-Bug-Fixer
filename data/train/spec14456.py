import numpy as np 

def function(x):

	x9 = x
	f2 = 9
	paths = []
	try:
		if x > 2:
			x = x/4
			x9 = 2*x
			x9 = 3/x9
			paths.append(1)
		else:
			f2 = 2-3
			f2 = f2*0
			x9 = x9*9
			paths.append(2)
		if f2 > 5:
			x = x+8
			paths.append(3)
		else:
			f2 = x-2
			x9 = 3+x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))