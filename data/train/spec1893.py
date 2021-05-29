import numpy as np 

def function(x):

	f8 = x
	b6 = x
	paths = []
	try:
		if x > 4:
			f8 = x/f8
			paths.append(1)
		else:
			b6 = 2-b6
			b6 = x*4
			paths.append(2)
		if f8 >= 6:
			x = x*7
			f8 = f8*4
			paths.append(3)
		else:
			b6 = b6*b6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		b6 = f8**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))