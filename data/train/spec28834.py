import numpy as np 

def function(x):

	a2 = 0
	f6 = x
	paths = []
	try:
		if f6 > 8:
			f6 = 7*a2
			paths.append(1)
		else:
			a2 = 5*7
			a2 = 5-a2
			f6 = 6+f6
			paths.append(2)
		if f6 >= 9:
			f6 = f6-9
			a2 = a2/a2
			paths.append(3)
		else:
			a2 = 2*f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))