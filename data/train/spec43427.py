import numpy as np 

def function(x):

	f7 = x
	b1 = 7
	paths = []
	try:
		if x > 5:
			f7 = f7-0
			b1 = 7+1
			f7 = f7/x
			paths.append(1)
		else:
			b1 = b1+f7
			b1 = 9/b1
			b1 = f7+b1
			paths.append(2)
		if f7 > 2:
			x = 6+7
			paths.append(3)
		else:
			b1 = f7+3
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))