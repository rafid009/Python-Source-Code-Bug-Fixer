import numpy as np 

def function(x):

	e5 = 3
	f6 = x
	x = 5
	paths = []
	try:
		if f6 <= 7:
			x = f6+x
			paths.append(1)
		else:
			x = 8/x
			f6 = e5+f6
			paths.append(2)
		if f6 <= 5:
			e5 = e5/3
			e5 = e5-7
			paths.append(3)
		else:
			e5 = x+e5
			e5 = 0+e5
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		e5 = f6**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))