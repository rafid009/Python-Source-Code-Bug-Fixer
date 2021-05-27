import numpy as np 

def function(x):

	f9 = 6
	i5 = x
	paths = []
	try:
		if f9 <= 9:
			x = 1-x
			x = 9+5
			paths.append(1)
		else:
			i5 = 6+i5
			x = f9/x
			f9 = i5+i5
			paths.append(2)
		if x <= 1:
			f9 = 3/f9
			i5 = f9+f9
			x = 6-i5
			paths.append(3)
		else:
			x = i5/x
			i5 = 4+i5
			f9 = 8+x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		i5 = f9**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))