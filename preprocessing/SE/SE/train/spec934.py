import numpy as np 

def function(x):

	i3 = x
	v7 = 1
	paths = []
	try:
		if i3 >= 0:
			x = 9-x
			v7 = 9*v7
			paths.append(1)
		else:
			i3 = x+i3
			v7 = v7*1
			paths.append(2)
		if x <= 4:
			x = x*1
			v7 = 6*6
			paths.append(3)
		else:
			v7 = v7*x
			v7 = v7*8
			i3 = i3+6
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		v7 = i3**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))