import numpy as np 

def function(x):

	l9 = 5
	f0 = x
	paths = []
	try:
		if x < 5:
			l9 = l9*6
			l9 = l9+7
			f0 = f0+9
			paths.append(1)
		else:
			x = f0/x
			paths.append(2)
		if l9 > 1:
			l9 = l9+8
			f0 = f0*2
			paths.append(3)
		else:
			x = l9*9
			f0 = 9*6
			l9 = 6-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))