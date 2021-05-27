import numpy as np 

def function(x):

	i8 = 9
	r5 = 6
	paths = []
	try:
		if i8 <= 7:
			i8 = i8/1
			paths.append(1)
		else:
			i8 = i8+x
			paths.append(2)
		if x < 4:
			x = 4-r5
			r5 = 9+3
			r5 = 2+x
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		r5 = i8**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))