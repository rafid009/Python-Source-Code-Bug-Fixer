import numpy as np 

def function(x):

	f2 = x
	l3 = x
	paths = []
	try:
		if x <= 1:
			f2 = f2/6
			x = 1/x
			l3 = l3*4
			paths.append(1)
		else:
			f2 = 2+f2
			f2 = f2*x
			x = 0/f2
			paths.append(2)
		if x > 2:
			x = 3+x
			paths.append(3)
		else:
			x = l3+f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))