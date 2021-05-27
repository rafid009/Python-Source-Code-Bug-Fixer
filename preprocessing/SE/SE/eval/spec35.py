import numpy as np 

def function(x):

	l5 = x
	f0 = 9
	paths = []
	try:
		if x <= 7:
			x = x+9
			paths.append(1)
		else:
			x = x*8
			x = x-f0
			paths.append(2)
		if f0 < 3:
			l5 = l5*9
			l5 = 5/7
			x = 3*x
			paths.append(3)
		else:
			f0 = f0+f0
			f0 = l5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))