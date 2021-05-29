import numpy as np 

def function(x):

	i3 = x
	j6 = 4
	paths = []
	try:
		if j6 >= 9:
			i3 = i3*4
			paths.append(1)
		else:
			x = 9/x
			j6 = 6+j6
			paths.append(2)
		if j6 >= 6:
			j6 = j6*0
			x = 2*x
			j6 = x*j6
			paths.append(3)
		else:
			x = i3/x
			i3 = 6-8
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))