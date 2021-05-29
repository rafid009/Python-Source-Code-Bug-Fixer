import numpy as np 

def function(x):

	b5 = x
	f1 = x
	paths = []
	try:
		if b5 < 3:
			b5 = x/1
			x = 2*x
			x = b5-x
			paths.append(1)
		else:
			f1 = 1-7
			b5 = 4/b5
			b5 = 8*f1
			paths.append(2)
		if b5 > 6:
			x = x/7
			paths.append(3)
		else:
			f1 = f1*3
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