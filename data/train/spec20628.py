import numpy as np 

def function(x):

	l7 = x
	f2 = 6
	paths = []
	try:
		if l7 <= 0:
			f2 = 7/f2
			f2 = x-f2
			paths.append(1)
		else:
			l7 = f2/f2
			x = x/x
			paths.append(2)
		if x < 5:
			l7 = 7*f2
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		l7 = f2**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))