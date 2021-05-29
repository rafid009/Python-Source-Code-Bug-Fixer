import numpy as np 

def function(x):

	w8 = 9
	i7 = x
	paths = []
	try:
		if x < 3:
			w8 = i7/w8
			w8 = w8-0
			x = 0*x
			paths.append(1)
		else:
			x = x*8
			i7 = 4+i7
			paths.append(2)
		if i7 > 2:
			i7 = i7/1
			paths.append(3)
		else:
			x = w8/4
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		i7 = w8**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))