import numpy as np 

def function(x):

	f2 = 9
	l8 = x
	paths = []
	try:
		if x < 1:
			l8 = l8+l8
			f2 = 8*3
			f2 = f2/x
			paths.append(1)
		else:
			f2 = f2-7
			l8 = l8/3
			f2 = 4/l8
			paths.append(2)
		if l8 <= 7:
			x = 3/x
			f2 = f2+f2
			paths.append(3)
		else:
			l8 = 6/l8
			l8 = 6-5
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))