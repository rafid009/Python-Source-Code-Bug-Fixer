import numpy as np 

def function(x):

	o9 = x
	f6 = x
	x = 1
	paths = []
	try:
		if x <= 8:
			f6 = 5+f6
			paths.append(1)
		else:
			o9 = x-x
			paths.append(2)
		if f6 > 9:
			f6 = f6+0
			paths.append(3)
		else:
			x = x+0
			o9 = o9+0
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		o9 = f6**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))