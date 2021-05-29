import numpy as np 

def function(x):

	f7 = x
	a2 = 0
	x = 5
	paths = []
	try:
		if x > 1:
			x = x-3
			f7 = 9+5
			f7 = a2/6
			paths.append(1)
		else:
			f7 = f7*6
			x = f7-0
			paths.append(2)
		if x >= 5:
			x = a2*4
			a2 = 5-a2
			paths.append(3)
		else:
			f7 = 0-x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))