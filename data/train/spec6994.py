import numpy as np 

def function(x):

	f7 = x
	l0 = 9
	paths = []
	try:
		if x >= 8:
			x = 7-x
			paths.append(1)
		else:
			l0 = l0-6
			l0 = x/5
			paths.append(2)
		if l0 >= 2:
			f7 = 8-f7
			x = l0+x
			paths.append(3)
		else:
			x = f7*l0
			l0 = l0+4
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))