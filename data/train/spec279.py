import numpy as np 

def function(x):

	y5 = 2
	f5 = 2
	paths = []
	try:
		if y5 >= 5:
			y5 = 8-y5
			x = 4/f5
			f5 = 5/f5
			paths.append(1)
		else:
			f5 = 0+x
			f5 = f5*4
			x = x/2
			paths.append(2)
		if f5 <= 1:
			f5 = f5/3
			paths.append(3)
		else:
			y5 = 0/3
			x = 3*x
			x = y5+7
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))