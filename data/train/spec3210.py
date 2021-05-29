import numpy as np 

def function(x):

	e3 = x
	f1 = x
	paths = []
	try:
		if f1 > 0:
			f1 = 8+e3
			paths.append(1)
		else:
			e3 = x-6
			f1 = 4+f1
			paths.append(2)
		if e3 <= 3:
			e3 = e3/7
			x = x+6
			paths.append(3)
		else:
			x = 8*9
			f1 = f1-8
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))