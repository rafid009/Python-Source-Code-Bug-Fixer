import numpy as np 

def function(x):

	f3 = 8
	e6 = x
	paths = []
	try:
		if x < 5:
			f3 = 7+f3
			x = f3*4
			x = 6+x
			paths.append(1)
		else:
			f3 = f3-f3
			paths.append(2)
		if e6 < 2:
			x = x/4
			paths.append(3)
		else:
			e6 = x-e6
			e6 = 2+4
			f3 = 1-f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))