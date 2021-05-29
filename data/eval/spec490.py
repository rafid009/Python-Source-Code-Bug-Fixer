import numpy as np 

def function(x):

	a4 = 3
	f1 = x
	paths = []
	try:
		if a4 <= 0:
			f1 = f1*6
			paths.append(1)
		else:
			f1 = f1+2
			paths.append(2)
		if f1 > 9:
			x = f1+a4
			f1 = f1+x
			f1 = f1+7
			paths.append(3)
		else:
			a4 = a4-4
			f1 = 9+x
			a4 = x/9
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		f1 = a4**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))