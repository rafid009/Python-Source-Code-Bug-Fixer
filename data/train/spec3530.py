import numpy as np 

def function(x):

	f9 = x
	x3 = 5
	paths = []
	try:
		if f9 < 3:
			x = x/4
			x = x3-x
			paths.append(1)
		else:
			f9 = 5-f9
			paths.append(2)
		if f9 > 4:
			x = x+0
			f9 = x/f9
			paths.append(3)
		else:
			x3 = 2+f9
			x3 = x/x3
			f9 = f9*8
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x3 = f9**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))