import numpy as np 

def function(x):

	f1 = x
	y5 = 8
	x = x
	paths = []
	try:
		if f1 > 7:
			f1 = f1*x
			f1 = f1*1
			paths.append(1)
		else:
			f1 = 5/f1
			paths.append(2)
		if x >= 0:
			x = x/3
			paths.append(3)
		else:
			x = x/7
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