import numpy as np 

def function(x):

	j0 = 5
	i5 = 9
	paths = []
	try:
		if i5 >= 4:
			x = 0-j0
			paths.append(1)
		else:
			x = x*6
			x = x-x
			i5 = j0/j0
			paths.append(2)
		if i5 <= 3:
			x = x+x
			j0 = j0*1
			x = x-8
			paths.append(3)
		else:
			i5 = i5+i5
			j0 = j0*x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))