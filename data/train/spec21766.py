import numpy as np 

def function(x):

	i3 = 2
	a7 = 5
	paths = []
	try:
		if x > 0:
			a7 = 2+a7
			paths.append(1)
		else:
			x = 9*x
			i3 = 1*x
			a7 = a7+1
			paths.append(2)
		if a7 <= 4:
			i3 = 0/i3
			paths.append(3)
		else:
			x = a7*1
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))