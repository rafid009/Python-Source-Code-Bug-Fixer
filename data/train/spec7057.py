import numpy as np 

def function(x):

	f5 = 1
	j1 = x
	x = 2
	paths = []
	try:
		if j1 >= 4:
			x = x+j1
			f5 = 7*f5
			paths.append(1)
		else:
			f5 = f5/7
			x = 4*x
			f5 = f5*0
			paths.append(2)
		if j1 > 2:
			f5 = f5-4
			j1 = 5*j1
			j1 = 3+j1
			paths.append(3)
		else:
			x = x/j1
			f5 = f5*2
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))