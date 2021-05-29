import numpy as np 

def function(x):

	f2 = 4
	x7 = x
	x = x
	paths = []
	try:
		if f2 > 2:
			x = x*6
			paths.append(1)
		else:
			x = x*9
			x7 = 3-9
			paths.append(2)
		if x7 <= 2:
			x7 = 9-x7
			x = x*x7
			f2 = f2+x7
			paths.append(3)
		else:
			x7 = x7-f2
			x = x+1
			f2 = f2/x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))