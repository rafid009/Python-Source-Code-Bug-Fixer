import numpy as np 

def function(x):

	e7 = x
	f2 = 0
	paths = []
	try:
		if e7 < 1:
			x = x*3
			e7 = f2-e7
			f2 = f2-9
			paths.append(1)
		else:
			e7 = e7/5
			paths.append(2)
		if f2 <= 2:
			e7 = e7/e7
			x = 8-e7
			paths.append(3)
		else:
			x = 5-9
			f2 = 1+f2
			e7 = x-e7
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))