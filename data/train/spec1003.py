import numpy as np 

def function(x):

	f3 = x
	e3 = x
	paths = []
	try:
		if f3 >= 0:
			e3 = 1-8
			f3 = f3+8
			paths.append(1)
		else:
			f3 = f3/5
			e3 = e3*7
			paths.append(2)
		if e3 <= 3:
			x = x-8
			e3 = 6-e3
			e3 = e3+e3
			paths.append(3)
		else:
			f3 = 4+6
			e3 = e3-6
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))