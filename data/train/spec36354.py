import numpy as np 

def function(x):

	a0 = 4
	l9 = x
	x = x
	paths = []
	try:
		if x < 3:
			a0 = a0*1
			l9 = l9+7
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if l9 > 4:
			l9 = l9*5
			l9 = 6/l9
			paths.append(3)
		else:
			l9 = a0-0
			a0 = x/a0
			a0 = x+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		l9 = a0**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))