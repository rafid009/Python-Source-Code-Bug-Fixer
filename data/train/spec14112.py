import numpy as np 

def function(x):

	f4 = x
	a3 = x
	paths = []
	try:
		if a3 > 8:
			f4 = f4-0
			paths.append(1)
		else:
			x = x+0
			x = f4*8
			x = 5/x
			paths.append(2)
		if f4 >= 2:
			f4 = x/7
			x = x/3
			a3 = 1+a3
			paths.append(3)
		else:
			a3 = 2-f4
			a3 = 2*x
			a3 = a3+1
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))