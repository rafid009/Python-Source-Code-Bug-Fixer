import numpy as np 

def function(x):

	f7 = 0
	l2 = 9
	paths = []
	try:
		if f7 >= 4:
			l2 = 2/4
			x = x/l2
			x = 6/l2
			paths.append(1)
		else:
			f7 = 1*6
			paths.append(2)
		if l2 >= 4:
			f7 = 1+f7
			paths.append(3)
		else:
			f7 = f7+9
			x = x*x
			f7 = 0/f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))