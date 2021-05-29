import numpy as np 

def function(x):

	f1 = x
	r9 = 5
	paths = []
	try:
		if f1 > 5:
			r9 = x/4
			r9 = f1*r9
			f1 = x-f1
			paths.append(1)
		else:
			r9 = r9/5
			x = r9*x
			paths.append(2)
		if x < 6:
			f1 = f1*6
			x = f1-8
			paths.append(3)
		else:
			r9 = 9*5
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