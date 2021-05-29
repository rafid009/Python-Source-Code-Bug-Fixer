import numpy as np 

def function(x):

	i3 = 1
	j5 = 5
	paths = []
	try:
		if x < 9:
			j5 = 1-x
			j5 = 5/j5
			x = x+4
			paths.append(1)
		else:
			x = 7*x
			i3 = i3-0
			i3 = j5-i3
			paths.append(2)
		if i3 > 2:
			j5 = 2*j5
			paths.append(3)
		else:
			x = 8-9
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))