import numpy as np 

def function(x):

	b9 = x
	a4 = 5
	paths = []
	try:
		if b9 <= 4:
			b9 = 3-b9
			a4 = 2/3
			paths.append(1)
		else:
			x = x*b9
			x = x*0
			a4 = 3*6
			paths.append(2)
		if b9 < 3:
			x = x*b9
			b9 = b9-x
			b9 = a4/8
			paths.append(3)
		else:
			a4 = a4+1
			x = x-9
			b9 = b9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))