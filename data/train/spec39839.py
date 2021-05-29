import numpy as np 

def function(x):

	i5 = x
	r3 = x
	paths = []
	try:
		if i5 >= 3:
			i5 = i5/r3
			r3 = 4/r3
			i5 = 7*i5
			paths.append(1)
		else:
			i5 = i5*5
			r3 = 8-r3
			paths.append(2)
		if i5 < 6:
			r3 = 3-r3
			x = 6+5
			paths.append(3)
		else:
			i5 = i5/2
			i5 = i5+4
			r3 = 8+x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))