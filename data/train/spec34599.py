import numpy as np 

def function(x):

	f6 = 2
	f3 = x
	paths = []
	try:
		if f6 > 0:
			f6 = f3-f6
			x = 8+x
			x = f6/x
			paths.append(1)
		else:
			f6 = 0-f6
			f3 = f3-2
			f6 = f6+0
			paths.append(2)
		if x >= 1:
			x = x+f3
			paths.append(3)
		else:
			f3 = 0/x
			x = 6*0
			f3 = 8-f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))