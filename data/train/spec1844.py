import numpy as np 

def function(x):

	i8 = 7
	f2 = x
	paths = []
	try:
		if f2 >= 5:
			i8 = i8-6
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if x > 9:
			i8 = i8-8
			x = 5+x
			x = 4+2
			paths.append(3)
		else:
			i8 = i8/f2
			x = x+f2
			f2 = f2/f2
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))