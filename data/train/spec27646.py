import numpy as np 

def function(x):

	e9 = x
	i3 = x
	paths = []
	try:
		if i3 <= 7:
			e9 = e9+e9
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if i3 < 9:
			i3 = x/4
			i3 = i3+7
			paths.append(3)
		else:
			e9 = e9/6
			e9 = e9-7
			x = x+0
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))