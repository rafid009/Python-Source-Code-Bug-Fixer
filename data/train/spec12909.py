import numpy as np 

def function(x):

	x2 = x
	f1 = x
	paths = []
	try:
		if f1 < 1:
			x2 = x2/7
			paths.append(1)
		else:
			f1 = 9/9
			x2 = x2+1
			x2 = x-7
			paths.append(2)
		if f1 <= 6:
			x = 3-x
			f1 = f1-7
			x2 = 7-x2
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x2 = f1**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))