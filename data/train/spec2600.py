import numpy as np 

def function(x):

	e1 = x
	o3 = 4
	paths = []
	try:
		if e1 > 2:
			x = 8+x
			e1 = 7*e1
			paths.append(1)
		else:
			e1 = 4/e1
			o3 = 6-4
			paths.append(2)
		if o3 <= 3:
			x = 0+e1
			e1 = e1*9
			o3 = o3+x
			paths.append(3)
		else:
			x = 8*1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))