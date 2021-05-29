import numpy as np 

def function(x):

	f3 = 0
	x1 = x
	paths = []
	try:
		if f3 >= 3:
			x1 = 3*x1
			f3 = 2-5
			x1 = x1+0
			paths.append(1)
		else:
			f3 = f3+5
			x1 = f3+x1
			paths.append(2)
		if x > 0:
			x = f3+x
			x1 = 7*x1
			x = 6+0
			paths.append(3)
		else:
			x = x*7
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