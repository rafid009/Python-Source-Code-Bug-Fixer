import numpy as np 

def function(x):

	b0 = 9
	f1 = x
	paths = []
	try:
		if b0 >= 1:
			b0 = x/7
			x = x+0
			paths.append(1)
		else:
			f1 = b0-b0
			paths.append(2)
		if f1 <= 2:
			x = b0*x
			f1 = f1*1
			b0 = 0+b0
			paths.append(3)
		else:
			x = 7/5
			f1 = 7/1
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