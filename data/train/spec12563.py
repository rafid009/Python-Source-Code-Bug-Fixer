import numpy as np 

def function(x):

	i7 = 2
	i5 = x
	paths = []
	try:
		if i7 < 6:
			i7 = 5-i7
			i5 = 2+i5
			paths.append(1)
		else:
			i7 = i7/9
			i7 = i5/3
			i7 = i7-8
			paths.append(2)
		if i5 <= 2:
			i5 = 8*3
			i7 = i7-9
			paths.append(3)
		else:
			i7 = i5*i7
			i7 = 0-7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))