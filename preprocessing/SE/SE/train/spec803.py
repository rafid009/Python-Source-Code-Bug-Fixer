import numpy as np 

def function(x):

	u6 = 0
	f1 = x
	paths = []
	try:
		if f1 <= 9:
			x = 6*5
			x = 6*4
			u6 = 1-u6
			paths.append(1)
		else:
			f1 = f1+u6
			f1 = x/x
			paths.append(2)
		if f1 < 0:
			u6 = x+5
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))