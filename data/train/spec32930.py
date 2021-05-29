import numpy as np 

def function(x):

	f5 = x
	e8 = 6
	paths = []
	try:
		if f5 >= 6:
			f5 = f5/6
			paths.append(1)
		else:
			e8 = f5+9
			x = x*0
			paths.append(2)
		if f5 > 0:
			x = e8-3
			x = x-2
			f5 = 4+5
			paths.append(3)
		else:
			x = e8*2
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))