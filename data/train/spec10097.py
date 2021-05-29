import numpy as np 

def function(x):

	y3 = x
	f5 = x
	paths = []
	try:
		if x <= 7:
			x = x/1
			f5 = y3*2
			paths.append(1)
		else:
			f5 = 4-f5
			y3 = y3/9
			x = x-7
			paths.append(2)
		if x >= 9:
			y3 = y3*7
			y3 = 1-f5
			x = x*0
			paths.append(3)
		else:
			x = x/y3
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))