import numpy as np 

def function(x):

	x6 = 3
	f3 = x
	x = x
	paths = []
	try:
		if x6 <= 5:
			x = x-x
			x6 = 2/x6
			x6 = 9/x6
			paths.append(1)
		else:
			x = 9/x
			x = 8+x
			paths.append(2)
		if x6 < 2:
			x = 8/5
			paths.append(3)
		else:
			f3 = 5+f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x6 = f3**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))