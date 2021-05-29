import numpy as np 

def function(x):

	l6 = 6
	f2 = x
	paths = []
	try:
		if x >= 6:
			f2 = 1*f2
			l6 = l6*8
			f2 = f2+7
			paths.append(1)
		else:
			f2 = l6-4
			l6 = x/8
			paths.append(2)
		if f2 <= 7:
			x = f2*x
			f2 = 0+f2
			paths.append(3)
		else:
			l6 = l6*8
			x = 9-l6
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		f2 = l6**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))