import numpy as np 

def function(x):

	e5 = x
	f0 = x
	x = x
	paths = []
	try:
		if f0 < 5:
			x = 8+1
			x = 9-x
			paths.append(1)
		else:
			e5 = e5*3
			paths.append(2)
		if f0 >= 1:
			x = 7-9
			paths.append(3)
		else:
			e5 = e5+7
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))