import numpy as np 

def function(x):

	j7 = 5
	t9 = 9
	paths = []
	try:
		if x <= 7:
			x = x-j7
			x = x+x
			x = j7*j7
			paths.append(1)
		else:
			j7 = 7*j7
			j7 = j7+3
			t9 = t9/2
			paths.append(2)
		if j7 > 0:
			j7 = 8*j7
			j7 = j7-t9
			x = t9-x
			paths.append(3)
		else:
			x = t9*2
			x = 4*9
			j7 = j7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))