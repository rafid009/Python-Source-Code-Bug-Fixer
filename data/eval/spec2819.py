import numpy as np 

def function(x):

	b5 = x
	y3 = 2
	paths = []
	try:
		if b5 >= 2:
			y3 = y3-3
			b5 = 6+b5
			paths.append(1)
		else:
			y3 = y3*x
			y3 = x/7
			paths.append(2)
		if x < 3:
			y3 = 2+1
			b5 = 9-b5
			x = 2*0
			paths.append(3)
		else:
			x = 6-x
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