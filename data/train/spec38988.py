import numpy as np 

def function(x):

	f1 = 7
	f8 = x
	paths = []
	try:
		if x >= 4:
			x = f1+2
			f1 = x-f1
			paths.append(1)
		else:
			f1 = f1+8
			paths.append(2)
		if f8 > 8:
			f8 = f8/9
			f1 = f1*f8
			f1 = 7*8
			paths.append(3)
		else:
			f1 = f1-7
			f1 = 4/f1
			f8 = f8/1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f8 = f1**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))