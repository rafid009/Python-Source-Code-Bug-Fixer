import numpy as np 

def function(x):

	f3 = x
	l1 = x
	x = x
	paths = []
	try:
		if f3 >= 3:
			f3 = f3*4
			paths.append(1)
		else:
			l1 = l1-9
			paths.append(2)
		if f3 <= 8:
			f3 = f3+5
			x = x-7
			paths.append(3)
		else:
			x = l1*8
			x = x*2
			l1 = 1/l1
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