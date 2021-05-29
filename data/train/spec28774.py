import numpy as np 

def function(x):

	a7 = x
	f4 = 3
	paths = []
	try:
		if x <= 1:
			f4 = 0/a7
			f4 = x+1
			paths.append(1)
		else:
			x = x-4
			a7 = 6+f4
			paths.append(2)
		if a7 >= 0:
			a7 = 0/7
			x = x/f4
			f4 = f4+3
			paths.append(3)
		else:
			x = x/f4
			f4 = f4/9
			x = 1/9
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))