import numpy as np 

def function(x):

	a3 = 3
	i3 = x
	paths = []
	try:
		if i3 <= 2:
			a3 = a3/i3
			x = a3-x
			a3 = 7+a3
			paths.append(1)
		else:
			a3 = 5+a3
			i3 = 6/x
			a3 = a3+3
			paths.append(2)
		if x > 4:
			x = x-7
			a3 = a3/i3
			paths.append(3)
		else:
			a3 = a3+i3
			a3 = 4*0
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		i3 = a3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))