import numpy as np 

def function(x):

	e1 = x
	i3 = 5
	x = x
	paths = []
	try:
		if i3 <= 3:
			x = i3*e1
			paths.append(1)
		else:
			i3 = i3/2
			i3 = i3*x
			paths.append(2)
		if x <= 4:
			e1 = 7+e1
			x = e1*5
			paths.append(3)
		else:
			e1 = 0/x
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