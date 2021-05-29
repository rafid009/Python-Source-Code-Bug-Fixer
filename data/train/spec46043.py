import numpy as np 

def function(x):

	f3 = x
	p7 = 5
	paths = []
	try:
		if p7 >= 3:
			p7 = 0/p7
			f3 = p7/f3
			p7 = p7/2
			paths.append(1)
		else:
			f3 = f3-1
			f3 = f3+f3
			paths.append(2)
		if x <= 0:
			x = 6*x
			paths.append(3)
		else:
			f3 = f3*7
			x = x/7
			x = x-9
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