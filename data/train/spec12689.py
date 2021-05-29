import numpy as np 

def function(x):

	b4 = 9
	f3 = 5
	paths = []
	try:
		if b4 <= 4:
			b4 = 9+b4
			b4 = b4-1
			f3 = 0*f3
			paths.append(1)
		else:
			b4 = 9*0
			b4 = 9-b4
			b4 = b4/1
			paths.append(2)
		if f3 <= 6:
			b4 = b4+x
			paths.append(3)
		else:
			f3 = 2-f3
			f3 = f3-4
			f3 = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))