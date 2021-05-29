import numpy as np 

def function(x):

	l1 = x
	f3 = x
	paths = []
	try:
		if l1 >= 7:
			l1 = l1+4
			l1 = 0/l1
			f3 = x+l1
			paths.append(1)
		else:
			x = 8*x
			f3 = f3/f3
			paths.append(2)
		if x < 0:
			x = x+1
			x = x-f3
			paths.append(3)
		else:
			f3 = f3+f3
			x = 4+2
			l1 = l1/6
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