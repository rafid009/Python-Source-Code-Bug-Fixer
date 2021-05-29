import numpy as np 

def function(x):

	g7 = 0
	f1 = x
	paths = []
	try:
		if f1 <= 8:
			f1 = f1+7
			x = 1+x
			paths.append(1)
		else:
			f1 = f1/x
			paths.append(2)
		if x <= 9:
			x = x*8
			x = 4-x
			paths.append(3)
		else:
			f1 = 7-f1
			x = 2-8
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		g7 = f1**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))