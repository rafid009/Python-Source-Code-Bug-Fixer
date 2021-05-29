import numpy as np 

def function(x):

	e1 = x
	o7 = 7
	paths = []
	try:
		if e1 < 8:
			o7 = x*0
			e1 = 8/e1
			paths.append(1)
		else:
			o7 = e1*2
			x = x*3
			x = o7-3
			paths.append(2)
		if x > 6:
			x = o7/6
			e1 = 0/e1
			o7 = o7+e1
			paths.append(3)
		else:
			x = 7-9
			o7 = o7+e1
			x = x*6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		e1 = o7**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))