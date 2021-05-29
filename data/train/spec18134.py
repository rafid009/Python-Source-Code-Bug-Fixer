import numpy as np 

def function(x):

	f7 = x
	e5 = 6
	paths = []
	try:
		if x <= 4:
			x = 8/x
			e5 = e5+x
			paths.append(1)
		else:
			f7 = f7*0
			e5 = e5+4
			paths.append(2)
		if f7 < 1:
			x = x+8
			f7 = f7/5
			paths.append(3)
		else:
			f7 = e5-e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))