import numpy as np 

def function(x):

	e5 = x
	i7 = 0
	paths = []
	try:
		if x > 7:
			x = e5-x
			e5 = e5+e5
			e5 = e5-x
			paths.append(1)
		else:
			e5 = e5-7
			paths.append(2)
		if x <= 3:
			x = x+i7
			i7 = i7-i7
			i7 = 1+i7
			paths.append(3)
		else:
			e5 = 5-x
			e5 = e5*1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		i7 = e5**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))