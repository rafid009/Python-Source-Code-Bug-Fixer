import numpy as np 

def function(x):

	j2 = x
	j1 = 3
	paths = []
	try:
		if j1 > 1:
			x = x+6
			j1 = 1+j1
			j2 = j2+4
			paths.append(1)
		else:
			j1 = j1+2
			x = j2+2
			j1 = 9-j1
			paths.append(2)
		if j1 < 7:
			j1 = 0+j1
			j1 = j1/j1
			j1 = j1+x
			paths.append(3)
		else:
			j2 = 0/6
			x = x+x
			j1 = j1*5
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))