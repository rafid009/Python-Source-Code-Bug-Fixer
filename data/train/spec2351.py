import numpy as np 

def function(x):

	f6 = 1
	b0 = 5
	paths = []
	try:
		if x <= 5:
			b0 = b0-f6
			b0 = b0+b0
			b0 = f6+b0
			paths.append(1)
		else:
			b0 = 3*1
			b0 = 1*b0
			paths.append(2)
		if x >= 1:
			f6 = b0-f6
			f6 = 5-f6
			b0 = 4/5
			paths.append(3)
		else:
			x = 1/b0
			x = 7*f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))