import numpy as np 

def function(x):

	b4 = 2
	j1 = x
	paths = []
	try:
		if b4 <= 3:
			j1 = j1+0
			x = j1/4
			paths.append(1)
		else:
			b4 = b4*2
			paths.append(2)
		if x < 0:
			j1 = x+7
			b4 = x+6
			x = 4-x
			paths.append(3)
		else:
			x = b4-j1
			j1 = 6*x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))