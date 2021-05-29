import numpy as np 

def function(x):

	a0 = x
	a9 = x
	paths = []
	try:
		if a9 < 3:
			a0 = 3+a0
			a9 = x-8
			paths.append(1)
		else:
			a9 = 3+a9
			paths.append(2)
		if a9 > 9:
			a0 = 2-a0
			x = x*1
			a9 = 2+a9
			paths.append(3)
		else:
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))