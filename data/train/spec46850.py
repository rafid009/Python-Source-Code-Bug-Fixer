import numpy as np 

def function(x):

	a1 = 2
	f0 = x
	paths = []
	try:
		if f0 > 5:
			a1 = 2+1
			f0 = f0/6
			x = 9+9
			paths.append(1)
		else:
			f0 = 3+f0
			a1 = 9*a1
			paths.append(2)
		if x < 6:
			x = 1/f0
			a1 = a1+f0
			paths.append(3)
		else:
			a1 = a1*7
			x = a1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))