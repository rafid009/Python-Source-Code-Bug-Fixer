import numpy as np 

def function(x):

	f8 = x
	j1 = 3
	paths = []
	try:
		if j1 <= 3:
			x = 8*2
			j1 = j1/j1
			paths.append(1)
		else:
			f8 = 4*f8
			paths.append(2)
		if f8 >= 4:
			x = x+8
			paths.append(3)
		else:
			x = x+5
			j1 = 5*f8
			x = 6*3
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		f8 = j1**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))