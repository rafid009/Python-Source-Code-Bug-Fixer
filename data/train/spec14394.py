import numpy as np 

def function(x):

	w8 = x
	i0 = x
	paths = []
	try:
		if w8 > 7:
			x = x*9
			x = 2/w8
			paths.append(1)
		else:
			w8 = 7+8
			i0 = 8*i0
			i0 = 0+i0
			paths.append(2)
		if i0 <= 5:
			x = x+8
			w8 = 8+w8
			w8 = w8-i0
			paths.append(3)
		else:
			w8 = w8-6
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))