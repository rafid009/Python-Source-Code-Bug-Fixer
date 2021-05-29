import numpy as np 

def function(x):

	l9 = x
	i6 = x
	x = x
	paths = []
	try:
		if l9 > 8:
			l9 = 9+1
			paths.append(1)
		else:
			l9 = l9+1
			i6 = 4-i6
			paths.append(2)
		if i6 <= 3:
			x = i6+6
			paths.append(3)
		else:
			l9 = l9+0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))