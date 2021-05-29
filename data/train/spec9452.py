import numpy as np 

def function(x):

	f1 = 3
	o9 = x
	paths = []
	try:
		if f1 < 5:
			f1 = f1*4
			x = x+7
			f1 = 1*4
			paths.append(1)
		else:
			f1 = 0+f1
			o9 = f1/o9
			f1 = f1/f1
			paths.append(2)
		if x < 7:
			o9 = x/o9
			x = o9*1
			o9 = 1-o9
			paths.append(3)
		else:
			f1 = f1-f1
			o9 = 1/o9
			x = 8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))