import numpy as np 

def function(x):

	j5 = x
	f8 = 7
	x = 7
	paths = []
	try:
		if f8 <= 5:
			f8 = 4*f8
			j5 = f8+8
			paths.append(1)
		else:
			f8 = 3+x
			f8 = x/f8
			paths.append(2)
		if j5 > 3:
			j5 = j5-x
			paths.append(3)
		else:
			j5 = 3+3
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		f8 = j5**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))