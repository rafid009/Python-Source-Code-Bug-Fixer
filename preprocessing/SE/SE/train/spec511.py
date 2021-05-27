import numpy as np 

def function(x):

	j5 = x
	e5 = 4
	paths = []
	try:
		if e5 > 8:
			e5 = e5-4
			e5 = e5/e5
			e5 = 1*0
			paths.append(1)
		else:
			e5 = e5*x
			e5 = 3*2
			j5 = x*j5
			paths.append(2)
		if j5 > 8:
			e5 = 8/x
			j5 = e5/8
			x = x+7
			paths.append(3)
		else:
			j5 = 4*j5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))