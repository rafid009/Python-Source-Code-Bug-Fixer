import numpy as np 

def function(x):

	e9 = x
	f8 = x
	x = x
	paths = []
	try:
		if x <= 5:
			e9 = e9+6
			f8 = f8+7
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if e9 <= 8:
			e9 = f8*1
			f8 = 6-f8
			x = 0*4
			paths.append(3)
		else:
			e9 = x/e9
			e9 = 8+3
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))