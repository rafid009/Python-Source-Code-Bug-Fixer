import numpy as np 

def function(x):

	l5 = 9
	f7 = 5
	paths = []
	try:
		if l5 >= 0:
			x = 5-x
			f7 = 5*8
			f7 = 9-f7
			paths.append(1)
		else:
			l5 = l5+x
			paths.append(2)
		if l5 < 2:
			x = 9/x
			x = 0+x
			paths.append(3)
		else:
			l5 = f7+7
			l5 = l5/5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		l5 = f7**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))