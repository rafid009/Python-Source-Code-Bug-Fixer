import numpy as np 

def function(x):

	y1 = 1
	f1 = 7
	paths = []
	try:
		if y1 <= 3:
			y1 = y1+y1
			f1 = x*2
			x = x+3
			paths.append(1)
		else:
			x = x-x
			y1 = y1-4
			paths.append(2)
		if f1 < 3:
			x = x*1
			paths.append(3)
		else:
			x = y1/5
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		y1 = f1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))