import numpy as np 

def function(x):

	l2 = 3
	f3 = x
	paths = []
	try:
		if x < 1:
			f3 = 6-f3
			x = x*2
			paths.append(1)
		else:
			x = 1*6
			l2 = 5-f3
			paths.append(2)
		if l2 > 6:
			l2 = l2+x
			paths.append(3)
		else:
			f3 = 9+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))