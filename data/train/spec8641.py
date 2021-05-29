import numpy as np 

def function(x):

	g6 = 3
	j2 = x
	paths = []
	try:
		if j2 <= 5:
			x = 0+3
			g6 = j2-2
			g6 = g6+8
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x > 4:
			x = x/5
			paths.append(3)
		else:
			j2 = x-9
			j2 = 0+j2
			j2 = j2/9
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