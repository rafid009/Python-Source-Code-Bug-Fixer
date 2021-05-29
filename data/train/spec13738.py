import numpy as np 

def function(x):

	y3 = x
	f5 = 5
	paths = []
	try:
		if y3 <= 3:
			f5 = x+x
			y3 = f5+1
			paths.append(1)
		else:
			f5 = f5*x
			x = x*3
			paths.append(2)
		if f5 >= 4:
			y3 = y3+y3
			y3 = 8/f5
			y3 = 7*4
			paths.append(3)
		else:
			f5 = 4-9
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