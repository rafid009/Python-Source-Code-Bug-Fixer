import numpy as np 

def function(x):

	j5 = 6
	y7 = 5
	paths = []
	try:
		if y7 < 5:
			x = x*0
			j5 = j5*0
			x = 7*x
			paths.append(1)
		else:
			j5 = 4+5
			j5 = x-j5
			j5 = 2-9
			paths.append(2)
		if j5 > 0:
			j5 = x*2
			x = x/y7
			x = y7+6
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))