import numpy as np 

def function(x):

	b6 = x
	f1 = 6
	paths = []
	try:
		if f1 < 8:
			f1 = f1*5
			paths.append(1)
		else:
			f1 = f1/b6
			paths.append(2)
		if f1 > 4:
			f1 = f1/9
			f1 = 6/b6
			b6 = x+7
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		f1 = b6**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))