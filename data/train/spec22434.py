import numpy as np 

def function(x):

	i5 = 4
	j1 = 9
	paths = []
	try:
		if i5 < 1:
			j1 = 0-2
			paths.append(1)
		else:
			i5 = i5+x
			paths.append(2)
		if x <= 3:
			i5 = 9-j1
			i5 = x+i5
			x = j1*1
			paths.append(3)
		else:
			i5 = i5*2
			j1 = x-j1
			i5 = 2/i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))