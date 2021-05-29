import numpy as np 

def function(x):

	f5 = 5
	e2 = 1
	paths = []
	try:
		if x < 5:
			f5 = e2-f5
			paths.append(1)
		else:
			f5 = 3-7
			paths.append(2)
		if f5 > 5:
			e2 = e2-1
			e2 = e2/3
			paths.append(3)
		else:
			f5 = f5-e2
			x = x+2
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))