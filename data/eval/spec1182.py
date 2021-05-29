import numpy as np 

def function(x):

	l3 = x
	f1 = 7
	paths = []
	try:
		if x > 7:
			f1 = 2/f1
			l3 = 4-x
			paths.append(1)
		else:
			l3 = 7-x
			f1 = 3-f1
			paths.append(2)
		if l3 >= 5:
			x = x-8
			x = 3+f1
			x = x/4
			paths.append(3)
		else:
			l3 = 8/9
			f1 = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))