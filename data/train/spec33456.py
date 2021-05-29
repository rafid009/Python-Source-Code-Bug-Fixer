import numpy as np 

def function(x):

	f2 = 5
	g9 = 6
	paths = []
	try:
		if g9 <= 3:
			f2 = g9-3
			paths.append(1)
		else:
			f2 = f2*0
			paths.append(2)
		if g9 <= 8:
			f2 = 1*f2
			f2 = 7-x
			paths.append(3)
		else:
			x = x-1
			x = x+0
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))