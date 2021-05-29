import numpy as np 

def function(x):

	o7 = 2
	e6 = x
	paths = []
	try:
		if e6 <= 1:
			x = x/8
			e6 = 0*e6
			e6 = e6/1
			paths.append(1)
		else:
			o7 = 9-o7
			e6 = o7+x
			paths.append(2)
		if x < 7:
			x = x*3
			o7 = o7*e6
			o7 = 2-9
			paths.append(3)
		else:
			x = x*1
			o7 = o7+e6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		e6 = o7**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))