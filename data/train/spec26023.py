import numpy as np 

def function(x):

	n7 = x
	f2 = x
	paths = []
	try:
		if f2 <= 0:
			n7 = n7-1
			x = 8+5
			n7 = n7*n7
			paths.append(1)
		else:
			f2 = x+f2
			n7 = f2/3
			x = x/x
			paths.append(2)
		if n7 >= 5:
			x = f2/x
			x = x*1
			paths.append(3)
		else:
			x = 3*x
			n7 = n7/x
			f2 = 5/f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))