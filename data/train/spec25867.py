import numpy as np 

def function(x):

	e8 = 9
	f3 = x
	paths = []
	try:
		if e8 <= 5:
			e8 = e8-6
			x = x*0
			paths.append(1)
		else:
			f3 = x+0
			e8 = e8+8
			e8 = 8*e8
			paths.append(2)
		if f3 >= 9:
			x = 1/x
			paths.append(3)
		else:
			f3 = 4*f3
			e8 = e8/8
			e8 = e8-x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))