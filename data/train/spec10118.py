import numpy as np 

def function(x):

	j1 = x
	f3 = x
	x = 8
	paths = []
	try:
		if x >= 1:
			x = 9/9
			paths.append(1)
		else:
			x = 2+x
			x = x/4
			x = 8-x
			paths.append(2)
		if f3 > 5:
			f3 = 7+x
			f3 = f3-2
			j1 = j1-4
			paths.append(3)
		else:
			x = x-f3
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