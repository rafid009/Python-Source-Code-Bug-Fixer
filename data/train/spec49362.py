import numpy as np 

def function(x):

	a4 = x
	b1 = x
	paths = []
	try:
		if b1 <= 1:
			a4 = 0+x
			a4 = a4-a4
			x = 1/x
			paths.append(1)
		else:
			a4 = 0*0
			x = x-8
			paths.append(2)
		if a4 >= 4:
			a4 = a4*8
			b1 = 9/9
			b1 = b1-b1
			paths.append(3)
		else:
			a4 = 7/2
			a4 = a4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))