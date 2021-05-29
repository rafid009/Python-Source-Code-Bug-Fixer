import numpy as np 

def function(x):

	j9 = x
	j2 = x
	paths = []
	try:
		if x < 8:
			x = x/1
			j9 = j9/3
			paths.append(1)
		else:
			x = x+6
			j9 = 7+0
			paths.append(2)
		if j9 >= 8:
			x = x*2
			j2 = j2/j9
			x = j9/j2
			paths.append(3)
		else:
			x = x-9
			j2 = j2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))