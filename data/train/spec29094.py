import numpy as np 

def function(x):

	f2 = x
	f5 = 9
	paths = []
	try:
		if f2 > 4:
			f5 = x*1
			f2 = f2/6
			f5 = f5*0
			paths.append(1)
		else:
			x = x+x
			f5 = 5*1
			paths.append(2)
		if x < 2:
			f2 = f5-7
			x = x*3
			x = 0-f5
			paths.append(3)
		else:
			f2 = f2-f5
			x = f5-x
			f2 = 2*f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))