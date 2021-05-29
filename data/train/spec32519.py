import numpy as np 

def function(x):

	i7 = x
	j6 = 2
	paths = []
	try:
		if j6 < 1:
			i7 = x+i7
			i7 = 0*i7
			paths.append(1)
		else:
			i7 = i7+i7
			paths.append(2)
		if i7 <= 9:
			i7 = i7*8
			paths.append(3)
		else:
			j6 = j6+i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		j6 = i7**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))