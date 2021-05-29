import numpy as np 

def function(x):

	f7 = 4
	j2 = 9
	paths = []
	try:
		if f7 > 3:
			j2 = 3/j2
			paths.append(1)
		else:
			x = x+x
			x = x+3
			paths.append(2)
		if x >= 0:
			x = x*3
			j2 = x/f7
			x = x/f7
			paths.append(3)
		else:
			f7 = x+f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))