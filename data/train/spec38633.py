import numpy as np 

def function(x):

	f8 = x
	a2 = x
	paths = []
	try:
		if a2 < 4:
			x = 8*x
			f8 = 0/f8
			paths.append(1)
		else:
			a2 = a2/f8
			paths.append(2)
		if x < 9:
			a2 = a2/1
			a2 = a2*7
			paths.append(3)
		else:
			f8 = 0+f8
			x = x*a2
			f8 = 6/6
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))