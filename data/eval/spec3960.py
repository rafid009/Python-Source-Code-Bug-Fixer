import numpy as np 

def function(x):

	b8 = x
	f7 = 5
	paths = []
	try:
		if f7 > 2:
			b8 = x/b8
			paths.append(1)
		else:
			b8 = b8/9
			b8 = x+b8
			paths.append(2)
		if x > 5:
			b8 = b8+f7
			x = x+9
			x = x*5
			paths.append(3)
		else:
			b8 = b8/1
			x = x*2
			x = x-6
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