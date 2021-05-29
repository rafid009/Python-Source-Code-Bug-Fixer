import numpy as np 

def function(x):

	j6 = x
	i4 = 5
	x = 6
	paths = []
	try:
		if i4 >= 7:
			j6 = j6+0
			i4 = 4+i4
			paths.append(1)
		else:
			i4 = x-8
			i4 = 1/i4
			paths.append(2)
		if i4 > 6:
			j6 = j6/3
			j6 = 9*j6
			paths.append(3)
		else:
			x = 7*i4
			i4 = i4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))