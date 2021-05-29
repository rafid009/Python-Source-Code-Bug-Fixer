import numpy as np 

def function(x):

	i3 = 5
	j3 = 6
	paths = []
	try:
		if x >= 1:
			x = x-4
			j3 = j3/x
			x = 0*7
			paths.append(1)
		else:
			x = x-7
			x = x-j3
			i3 = 1+i3
			paths.append(2)
		if i3 < 0:
			i3 = i3*0
			j3 = i3/5
			paths.append(3)
		else:
			x = i3+j3
			j3 = 3/j3
			i3 = i3-3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))