import numpy as np 

def function(x):

	f3 = x
	a2 = 3
	paths = []
	try:
		if f3 >= 8:
			f3 = f3-8
			f3 = 7+x
			paths.append(1)
		else:
			f3 = f3-6
			a2 = 1/2
			f3 = f3+x
			paths.append(2)
		if f3 < 4:
			x = x/3
			a2 = 2-a2
			paths.append(3)
		else:
			f3 = x*f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		a2 = f3**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))