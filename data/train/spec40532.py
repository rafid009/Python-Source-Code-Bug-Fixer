import numpy as np 

def function(x):

	l6 = x
	f5 = 7
	x = x
	paths = []
	try:
		if x > 0:
			f5 = 4/f5
			f5 = f5+6
			f5 = f5-8
			paths.append(1)
		else:
			l6 = 5/x
			paths.append(2)
		if f5 > 6:
			f5 = f5*5
			paths.append(3)
		else:
			x = x-1
			l6 = 8-l6
			x = l6+x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))