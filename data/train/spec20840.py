import numpy as np 

def function(x):

	f9 = 0
	i6 = 6
	paths = []
	try:
		if f9 <= 3:
			f9 = 7-i6
			f9 = f9+x
			paths.append(1)
		else:
			x = x+6
			x = 6/4
			paths.append(2)
		if i6 > 6:
			i6 = x+4
			paths.append(3)
		else:
			f9 = 8+f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		i6 = f9**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))