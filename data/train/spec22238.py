import numpy as np 

def function(x):

	f8 = x
	l5 = 2
	paths = []
	try:
		if f8 < 6:
			l5 = l5-l5
			l5 = l5/f8
			paths.append(1)
		else:
			l5 = l5-x
			x = f8-x
			paths.append(2)
		if l5 < 0:
			f8 = x-f8
			paths.append(3)
		else:
			f8 = 4/f8
			f8 = 5+2
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))