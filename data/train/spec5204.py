import numpy as np 

def function(x):

	f9 = x
	a6 = x
	paths = []
	try:
		if a6 <= 0:
			a6 = 5/x
			x = 2*5
			a6 = x/a6
			paths.append(1)
		else:
			x = 9+x
			x = x-9
			f9 = f9/8
			paths.append(2)
		if a6 < 8:
			f9 = 0-1
			a6 = 4+a6
			a6 = 8*f9
			paths.append(3)
		else:
			x = x/8
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))