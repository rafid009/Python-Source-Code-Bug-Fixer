import numpy as np 

def function(x):

	i3 = x
	w7 = 7
	paths = []
	try:
		if i3 <= 4:
			x = x-1
			x = i3+9
			x = x/2
			paths.append(1)
		else:
			x = x*w7
			w7 = w7*4
			w7 = w7-w7
			paths.append(2)
		if i3 < 1:
			x = x/3
			w7 = 2/2
			paths.append(3)
		else:
			x = 0-3
			w7 = w7+w7
			x = x/9
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))