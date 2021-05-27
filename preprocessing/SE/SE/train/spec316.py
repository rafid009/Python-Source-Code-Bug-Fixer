import numpy as np 

def function(x):

	b1 = 4
	j1 = x
	paths = []
	try:
		if j1 < 3:
			x = x*5
			x = 7/j1
			paths.append(1)
		else:
			b1 = j1*b1
			x = 8*0
			j1 = j1*j1
			paths.append(2)
		if x < 3:
			b1 = 3*j1
			x = b1+x
			b1 = b1-9
			paths.append(3)
		else:
			j1 = 2/b1
			x = 2+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))