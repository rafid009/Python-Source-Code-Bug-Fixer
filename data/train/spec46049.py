import numpy as np 

def function(x):

	w8 = x
	i3 = x
	paths = []
	try:
		if i3 < 6:
			i3 = i3-2
			paths.append(1)
		else:
			i3 = 8+x
			i3 = i3-3
			paths.append(2)
		if w8 < 4:
			i3 = 8-w8
			w8 = 8+w8
			w8 = x-1
			paths.append(3)
		else:
			i3 = i3+i3
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))