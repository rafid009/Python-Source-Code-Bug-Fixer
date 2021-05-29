import numpy as np 

def function(x):

	r3 = x
	j1 = 5
	paths = []
	try:
		if j1 >= 5:
			r3 = r3+4
			x = x/r3
			paths.append(1)
		else:
			x = x+8
			j1 = j1/4
			x = x*2
			paths.append(2)
		if x < 9:
			x = x/x
			x = 4/9
			paths.append(3)
		else:
			r3 = 0-r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))