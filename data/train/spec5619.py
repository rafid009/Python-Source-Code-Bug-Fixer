import numpy as np 

def function(x):

	a8 = 1
	f1 = x
	paths = []
	try:
		if x <= 2:
			f1 = 7-f1
			a8 = a8-5
			paths.append(1)
		else:
			x = x-2
			x = x/a8
			x = f1+1
			paths.append(2)
		if x >= 6:
			f1 = f1/5
			f1 = f1*0
			paths.append(3)
		else:
			x = 9+f1
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		f1 = a8**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))