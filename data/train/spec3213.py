import numpy as np 

def function(x):

	a7 = 5
	f1 = 2
	paths = []
	try:
		if f1 < 6:
			x = x+9
			x = x*5
			x = 4/a7
			paths.append(1)
		else:
			a7 = a7+0
			a7 = a7/6
			paths.append(2)
		if a7 < 2:
			a7 = a7*a7
			a7 = x*4
			paths.append(3)
		else:
			f1 = f1/f1
			a7 = 7+7
			a7 = 9-a7
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